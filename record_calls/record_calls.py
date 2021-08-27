NO_RETURN = None


class Call:
    def __init__(self, args, kwargs, return_value, exception):
        self.args = args
        self.kwargs = kwargs
        self.return_value = return_value
        self.exception = exception

    def __repr__(self):
        return (f"Call(args={self.args}, kwargs={self.kwargs}, "
                f"return_value={self.return_value}, exception={self.exception})")


class record_calls(object):
    calls = []
    call_count = 0

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        try:
            return_value = self.func(*args, **kwargs)
            self.calls.append(
                Call(args, kwargs, return_value, None)
            )
            return return_value
        except Exception as e:
            self.calls.append(
                Call(args, kwargs, NO_RETURN, e)
            )
            raise e
