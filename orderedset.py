class OrderedSet:
    def __init__(self, list_of_values):
        self.values = list()
        for item in list_of_values:
            self.add(item)

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return set(self.values) == set(other.values)
        else:
            return set(self.values) == other

    def add(self, obj):
        if object not in self.values:
            self.values.append(obj)

    def discard(self, obj):
        if obj in self.values:
            idx = self.values.index(obj)
            print(idx)
            trash = self.values.pop(idx)
