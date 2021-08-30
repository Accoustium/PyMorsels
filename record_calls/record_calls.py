from typing import *
from dataclasses import dataclass
NO_RETURN = None


@dataclass(frozen=True)
class Call:
    args: tuple
    kwargs: dict
    return_value: Any
    exception: Optional[Exception]


class record_calls(object):
    def __init__(self, func):
        self.func = func
        self.calls = []
        self.call_count = 0

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
