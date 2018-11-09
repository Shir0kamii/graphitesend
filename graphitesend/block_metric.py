from contextlib import contextmanager, ExitStack
from time import time


@contextmanager
def executions(client, metric):
    try:
        yield
    finally:
        client.send(metric + ".executions", 1)


@contextmanager
def errors(client, metric):
    try:
        yield
    except Exception:
        client.send(metric + ".errors", 1)


@contextmanager
def processing_time(client, metric):
    start = time()
    try:
        yield
    finally:
        client.send(metric + ".processing_time", time() - start)


class BlockMetric:
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
