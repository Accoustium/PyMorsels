class window:
    def __init__(self, iterable: list, *step: int, fillvalue=None):
        self.iterable = iter(iterable)
        self.curr_list = []
        self.curr_iteration = 0
        self.step = step
        self.fill_value = fillvalue
        self.stop = False
        if len(self.step) > 1:
            raise TypeError
        else:
            self.step = self.step[0]

    def __iter__(self):
        return iter(list(self.generate_list()))

    def __next__(self):
        ...

    def generate_list(self):
        if self.step == 0:
            return None

        return_tuple = []
        while True:
            for stride in range(self.step):
                try:
                    return_tuple.append(self.curr_list[self.curr_iteration + stride])
                except IndexError:
                    try:
                        self.curr_list.append(next(self.iterable))
                        return_tuple.append(self.curr_list[self.curr_iteration + stride])
                    except StopIteration:
                        self.curr_list.append(self.fill_value)
                        self.stop = True
                        return_tuple.append(self.curr_list[self.curr_iteration + stride])

            if self.stop and self.curr_iteration == 0:
                yield tuple(return_tuple)
                break
            else:
                if not self.stop:
                    yield tuple(return_tuple)
                self.curr_iteration += 1
                return_tuple = []
                if self.stop:
                    break
