from time import time


class BlockMetric:

    def __init__(self, client, metric):
        self.client = client
        self.metric = metric

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.send(self.metric + ".executions", 1)
        if exc_type is not None:
            self.client.send(self.metric + ".errors", 1)
            return
        processing_time = time() - self.start
        self.client.send(self.metric + ".processing_time", processing_time)
