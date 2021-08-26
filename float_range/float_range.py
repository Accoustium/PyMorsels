class float_range:
    def __init__(self, start: float, stop: float = None, step: float = 1.0):
        if step == 0:
            raise ValueError

        self.step = float(step)
        self.__curr = None

        if stop is None and start:
            self.stop = float(start)
            self.start = 0.0
        else:
            self.start = float(start)
            self.stop = float(stop)

    def __repr__(self):
        return f"float_range({self.start}, {self.stop}, {self.step})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__curr is None:
            self.__curr = self.__step()
        return next(self.__curr)

    def __reversed__(self):
        new = list(self)
        return float_range(start=new[-1], stop=new[0] - self.step, step=self.step * -1)

    def __eq__(self, other):
        if isinstance(other, float_range) or isinstance(other, range):
            return self.start == other.start and self.stop == other.stop and self.step == other.step

        return False

    def __len__(self):
        if self.step > 0 and self.stop > self.start:
            return int(round((self.stop - self.start) / self.step, 0))
        elif self.step < 0 and self.start > self.stop:
            return int(round((self.start - self.stop) / (self.step * -1), 0))
        else:
            return 0

    def __step(self):
        v = self.start
        while (v < self.stop and self.step > 0) or (v > self.stop and self.step < 0):
            yield v
            v += self.step
