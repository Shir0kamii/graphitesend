import sys
from time import time

if sys.version_info.major == 2:
    from contextlib2 import contextmanager, ExitStack
else:
    from contextlib import contextmanager, ExitStack


@contextmanager
def executions(client, metric):
    """Track the number of executions"""
    try:
        yield
    finally:
        client.send(metric + ".executions", 1)


@contextmanager
def errors(client, metric):
    """Track the number of errors"""
    try:
        yield
    except Exception:
        client.send(metric + ".errors", 1)


@contextmanager
def processing_time(client, metric):
    """Track the processing time"""
    start = time()
    try:
        yield
    finally:
        client.send(metric + ".processing_time", time() - start)


class BlockMetric:
    """Enable tracking on a block of code"""

    #: Trackers activated during the execution of the block of code
    trackers = [executions, errors, processing_time]

    def __init__(self, client, metric):
        self.client = client
        self.metric = metric

    def __enter__(self):
        self.stack = ExitStack()
        for tracker in self.trackers:
            self.stack.enter_context(tracker(self.client, self.metric))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stack.__exit__(exc_type, exc_val, exc_tb)
