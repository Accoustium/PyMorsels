from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *exceptions):
        self.exceptions = exceptions
        self.exception = None
        self.traceback = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if (
                exc_type not in self.exceptions and
                set(exc_type.__bases__).intersection(
                    set(
                        [self.exceptions]
                        if type(self.exceptions) != tuple
                        else self.exceptions
                    )
                ) == set()
            ):
                raise exc_val

            self.exception = exc_val
            self.traceback = exc_tb

        return self
