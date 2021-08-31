from typing import *


class interleave:
    def __init__(self, *args):
        self.args: Generator = args
        self.idx: int = 0
        self.max_idx: int = max(map(lambda x: len(x), args))

    def __iter__(self):
        return self

    def __next__(self):
        num = next(self.__step())
        return num

    def __step(self):
        while self.idx < self.max_idx:
            for leave in self.args:
                try:
                    yield next(leave)
                except StopIteration:
                    pass

            self.idx += 1
