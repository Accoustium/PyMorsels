class float_range:
    def __init__(self, start: float, stop: float = None, step: float = 1.0):
        if step == 0.0:
            raise ValueError

        self.step = float(step)
        self.__curr = None

        if stop is None and start:
            self.stop = float(start)
            self.start = 0.0
        else:
            self.start = float(start)
            self.stop = float(stop)

    def __iter__(self):
        return FloatRangeIterator(self)

    def __repr__(self):
        return f"float_range({self.start}, {self.stop}, {self.step})"

    def __reversed__(self):
        return iter(float_range(start=self.__find_last(), stop=self.start - self.step, step=self.step * -1))

    def __eq__(self, other):
        if isinstance(other, float_range):
            return self.start == other.start and self.__find_last() == other.__find_last() and self.step == other.step

        return all([self.start == other, self.stop == other, self.step == other])

    def __len__(self):
        if self.step > 0 and self.stop > self.start:
            return int(round((self.stop - self.start) / self.step, 0))
        elif self.step < 0 and self.start > self.stop:
            return int(round((self.start - self.stop) / (self.step * -1), 0))

        return 0

    def __find_last(self):
        return (len(self) - 1) * self.step + self.start


class FloatRangeIterator:
    def __init__(self, range_float: float_range):
        self.float_range = range_float
        self.__curr = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__curr is None:
            self.__curr = self.__step()
        return next(self.__curr)

    def __step(self):
        v = self.float_range.start
        while (
                (v < self.float_range.stop and self.float_range.step > 0) or
                (v > self.float_range.stop and self.float_range.step < 0)
        ):
            yield v
            v += self.float_range.step
