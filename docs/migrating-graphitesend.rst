Migrating from graphitesend
###########################

To migrate from graphitesend to graphitesender, you must make the following
changes.

Metric formatting
=================

In graphitesend, there was a myriad of arguments you could pass to the client to
roughly customize the metric formatting. Now, they'll disappear in
graphitesender so you'll have to pass the *formatter* argument instead.

It should be a callable that takes a metric name and output a formatted metric
name ready to be sent. You can still pass a :class:`GraphiteStructuredFormatter
<graphitesend.formatter.GraphiteStructuredFormatter>` instance if you want to
keep the old behavior.

.. note::

    Passing the formatting arguments to the client still works, but it's
    deprecated and will be removed in a future version.
