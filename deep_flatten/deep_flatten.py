class deep_flatten:
    def __init__(self, iterable):
        self.iterable = iterable
        self.curr = self.flatten(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        num = next(self.curr)
        return num

    def flatten(self, iter_):
        if type(iter_) == int or type(iter_) == str:
            yield iter_

        for iterable_ in iter_:
            if type(iterable_) == int or type(iterable_) == str:
                yield iterable_
            else:
                yield from self.flatten(iterable_)
