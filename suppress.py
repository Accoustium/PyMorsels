import sys


class suppress:
    def __init__(self, *exceptions):
        try:
            pass
        except exceptions:
            self.exception = sys.exc_info()[1]
            self.traceback = sys.exc_info()[2]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self
