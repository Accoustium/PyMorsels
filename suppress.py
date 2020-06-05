import sys
from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *exceptions):
        self.exceptions = exceptions
        try:
            pass
        except self.exceptions:
            self.exception = sys.exc_info()[1]
            self.traceback = sys.exc_info()[2]
