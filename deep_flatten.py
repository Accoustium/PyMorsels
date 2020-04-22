class deep_flatten:
    def __init__(self, iterable: list):
        self.iterable = iter(iterable)
        self.output = []

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return next(iter(self.output))
            except StopIteration:
                next(iter(self.flatten(self.iterable)))

    def flatten(self, iterable):
        for item in iterable:
            if isinstance(item, (str, int)):
                self.output.append(item)
                yield
            else:
                self.flatten(item)