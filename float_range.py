class float_range:
    def init(self, start, stop, step):
        if not step:
            self.step = 1

        if not stop and start:
            self.stop = start
            self.start = 0
        ...

    def __get__(self):
        ...
