import math


class Circle:
    def __init__(self, val = 1):
        self._radius = val

    def __str__(self):
        return f"Circle({self._radius})"

    def __repr__(self):
        return f"Circle({self._radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("Radius cannot be negative")

        self._radius = val
        return self._radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2
        return self._radius * 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @area.setter
    def area(self, val):
        raise AttributeError()
