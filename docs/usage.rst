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

Measuring the execution of a function
=====================================

You can retrieve the same metrics for a function using the
:meth:`decorator <graphitesend.graphitesend.GraphiteClient.decorator>` method of
the client.

.. code-block:: python

    @cient.decorator
    def foo():
        pass

The following form, without argument, will use the name of the function as a
base metric name. In this case, it will be *foo.executions* and so on.

.. code-block:: python

    @client.decorator("bar")
    def foo():
        pass

This second sample will send the metrics with the base metric name *bar*.
