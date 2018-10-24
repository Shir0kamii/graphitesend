Advanced usage
##############

Sending dicts and lists
=======================

:meth:`send_dict <graphitesend.graphitesend.GraphiteClient.send_dict>` and
:meth:`send_list <graphitesend.graphitesend.GraphiteClient.send_list>` can be
used to send dicts and lists.

Measuring the execution of a block of code
==========================================

The :meth:`metric_block <graphitesend.graphitesend.GraphiteClient.block_metric>`
method can be used as context manager to retrieve metrics on the execution of a
block of code.

.. code-block:: python

    with client.block_metric("foo"):
        ...

This sample of code will send the following metrics (before formatting is
applied):

* *foo.executions* with a value of 1
* If an exception was raised
    * *foo.errors* with a value of 1
* Else
    * *foo.processing_time* with a value representing the time the block took to
      execute

The responsability is yours to agregate the metrics, for example with
carbon-aggregate.


