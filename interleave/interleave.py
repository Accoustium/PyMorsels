class interleave:
    def __init__(self, *args):
        self.args: list = [iter(x) for x in args]
        self.gen = self.__step()

    def __iter__(self):
        return self

    def __next__(self):
        num = next(self.gen)
        return num

    def __step(self):
        while True:
            count, length = 0, 0
            for leave in self.args:
                length += 1
                try:
                    yield next(leave)
                except StopIteration:
                    count += 1

            if count == length:
                break
