class OrderedSet:
    def __init__(self, list_of_values):
        self.values = list()
        self.set_values = set()
        self.gen = None
        for item in list_of_values:
            self.add(item)

    def __str__(self):
        return self.values

    def __getitem__(self, item):
        return self.values[item]

    def __iter__(self):
        if self.gen is None:
            self.gen = (x for x in self.values)

        return self.gen

    def __len__(self):
        return len(self.values)

    def __eq__(self, other):
        if isinstance(other, OrderedSet) is True:
            return self.values == other.values
        else:
            return set(self.values) == other

    def __contains__(self, item):
        return item in self.set_values

    def add(self, obj):
        if obj not in self.set_values:
            self.values.append(obj)
            self.set_values.add(obj)

    def discard(self, obj):
        if obj in self.values:
            self.set_values.remove(obj)
            idx = self.values.index(obj)
            trash = self.values.pop(idx)
