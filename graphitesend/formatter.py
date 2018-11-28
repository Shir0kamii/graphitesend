import logging
import platform

log = logging.getLogger("graphitesend")


class TemplateFormatter:
    """Formatter based on a template string

    :param template: A template string that will be rendered for each metric

    Additionnal keyword arguments must be callable, they will be called during
    rendering with the metric name and should return a string.

    The template must use the modern python formatting syntax, but does not
    support ordered placeholders. The formatting data will consist of the
    result of the functions given during instanciation, plus special variables:

    * name: The name of the metric
    * host: The system's node name

    Consider the following example:

    >>> formatter = TemplateFormatter("systems.{host}.worker{worker}.{name}",
                                      worker=get_worker_id)

    On a machine named *foobar* and assuming a *get_worker_id* function that
    return an id, the metric "processing_time" would be formatted like
    "systems.foobar.worker3.processing_time".
    """

    def __init__(self, template, **kwargs):
        self.template = template
        self.context_getters = {
            "host": lambda _: platform.node(),
        }
        self.context_getters.update(kwargs)

    def make_context(self, metric_name):
        return {key: value(metric_name)
                for key, value in self.context_getters.items()}

    def __call__(self, name):
        context = self.make_context(name)
        return self.template.format(name=name, **context)


class GraphiteStructuredFormatter(object):
    '''Default formatter for GraphiteClient.

    Provides structured metric naming based on a prefix, system name, group, etc

    :param prefix: string added to the start of all metrics
    :type prefix: Default: "systems."
    :param group: string added to after system_name and before metric name
    :param system_name: FDQN of the system generating the metrics
    :type system_name: Default: current FDQN
    :param suffix: string added to the end of all metrics
    :param lowercase_metric_names: Toggle the .lower() of all metric names
    :param fqdn_squash: Change host.example.com to host_example_com
    :type fqdn_squash: True or False
    :param clean_metric_name: Does GraphiteClient needs to clean metric's name
    :type clean_metric_name: True or False

    Feel free to implement your own formatter as any callable that accepts a
    metric name as argument and return a formatted metric name.
    '''

    cleaning_replacement_list = [
        ('(', '_'),
        (')', ''),
        (' ', '_'),
        ('/', '_'),
        ('\\', '_')
    ]

    def __init__(self, prefix=None, group=None, system_name=None, suffix=None,
                 lowercase_metric_names=False, fqdn_squash=False, clean_metric_name=True):

        prefix_parts = []

        if prefix != '':
            prefix = prefix or "systems"
            prefix_parts.append(prefix)

        if system_name != '':
            system_name = system_name or platform.uname()[1]
            if fqdn_squash:
                system_name = system_name.replace('.', '_')
            prefix_parts.append(system_name)

        if group is not None:
            prefix_parts.append(group)

        prefix = '.'.join(prefix_parts)
        prefix = prefix.replace('..', '.')  # remove double dots
        prefix = prefix.replace(' ', '_')  # Replace ' 'spaces with _
        if prefix:
            prefix += '.'
        self.prefix = prefix

        self.suffix = suffix or ""
        self.lowercase_metric_names = lowercase_metric_names
        self._clean_metric_name = clean_metric_name

    def clean_metric_name(self, metric_name):
        """
        Make sure the metric is free of control chars, spaces, tabs, etc.
        """
        if not self._clean_metric_name:
            return metric_name
        metric_name = str(metric_name)
        for _from, _to in self.cleaning_replacement_list:
            metric_name = metric_name.replace(_from, _to)
        return metric_name

    def __call__(self, metric_name):
        '''Format a metric, value, and timestamp for use on the carbon text socket.'''
        log.debug("metric: '%s'" % metric_name)
        metric_name = self.clean_metric_name(metric_name)
        log.debug("metric: '%s'" % metric_name)

        message = "{}{}{}".format(self.prefix, metric_name, self.suffix)

        # An option to lowercase the entire message
        if self.lowercase_metric_names:
            message = message.lower()

        return message
