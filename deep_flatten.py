class deep_flatten:
    def __init__(self, iterable: list):
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        yield from self.flatten(self.iterable)

    def flatten(self, iter_):
        for iterable_ in iter_:
            if type(iterable_) == list or type(iterable_) == tuple:
                yield from self.flatten(iterable_)
            else:
                yield iterable_
