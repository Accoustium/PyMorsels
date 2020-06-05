class compact:
    def __init__(self, param):
        self.param = param
        self.prev = None
        self.curr = self.compact()

    def __iter__(self):
        return self

    def __next__(self):
        num = next(self.curr)
        return num

    def compact(self):
        for ind, val in enumerate(self.param):
            if ind > 0:
                if val == self.prev:
                    continue
            self.prev = val
            yield self.prev
