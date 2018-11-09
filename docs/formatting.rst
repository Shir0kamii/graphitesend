Metrics formatting
##################

Metrics are formatted before they are sent to Graphite.

Default formatting
==================

When you send a metric *foobar* on a machine named *robocop*, the metric will be
formatted to *systems.robocop.foobar*.

Custom formatting
=================

You can customize the formatting by giving a callable to the *formatter*
argument of the client.

The best way to have a custom output is to pass a :class:`TemplateFormatter
<graphitesend.formatter.TemplateFormatter>` instance to the client.

If you don't give one, the following arguments of the client will be forwarded
to the :class:`GraphiteStructuredFormatter
<graphitesend.formatter.GraphiteStructuredFormatter>` to make a formatter:

* prefix
* group
* system_name
* suffix
* lowercase_metric_names
* fqdn_squash
* clean_metric_name

.. warning::

    These arguments are deprecated and will soon be removed from the client.
    You can instead instantiate the :class:`GraphiteStructuredFormatter
    <graphitesend.formatter.GraphiteStructuredFormatter>` and pass it to the
    client.
