class deep_flatten:
    def __init__(self, iterable: list):
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(iter(self.flatten(self.iterable)))

    def flatten(self, iterable):
        for item in iterable:
            if isinstance(item, (str, int)):
                yield item
            else:
                yield from self.flatten(item)