class CyclicList(list):
    idx = 0

    def __iter__(self):
        return CyclicListIterator(self)

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start if item.start else 0
            if not item.stop:
                if start >= 0:
                    stop = len(self)
                else:
                    stop = 0
            else:
                stop = item.stop
            step = item.step if item.step else 1

            return [self[x] for x in range(start, stop, step)]
        else:
            return super(CyclicList, self).__getitem__(self.clean_index(item))

    def __setitem__(self, key, value):
        super(CyclicList, self).__setitem__(self.clean_index(key), value)

    def clean_index(self, item):
        if isinstance(item, int):
            return item % len(self) if item > 0 else -1 * (abs(item) % len(self))


class CyclicListIterator:
    idx = 0

    def __init__(self, cycle: CyclicList):
        self.cycle = cycle

    def __iter__(self):
        return self

    def __next__(self):
        num = self.cycle[self.idx]
        self.idx += 1
        return num
