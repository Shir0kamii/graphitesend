Metrics formatting
##################

Metrics are formatted before they are sent to Graphite.

This is controlled by the following arguments of the client:

* prefix
* group
* system_name
* suffix
* lowercase_metric_names
* fqdn_squash
* clean_metric_name

These arguments are forwarded to the formatter. You can read about their effects
:class:`there <graphitesend.formatter.GraphiteStructuredFormatter>`
