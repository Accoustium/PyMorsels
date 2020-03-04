class OrderedSet:
    def __init__(self, order: list):
        ...

    def __iter__(self):
        yield from self

    def __str__(self):
        return list()

    def __eq__(self, other):
        if not isinstance(other, OrderedSet):
            return NotImplemented
        return list(self) == list(other)

    def add(self, value):
        ...

    def discard(self, value):
        ...
