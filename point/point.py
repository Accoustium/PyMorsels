class Point():
    def __str__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        z1 = self.z + other.z

        return Point(x1, y1, z1)

    def __sub__(self, other):
        x1 = self.x - other.x
        y1 = self.y - other.y
        z1 = self.z - other.z

        return Point(x1, y1, z1)

    def __mul__(self, other):
        if type(other) == int:
            x1 = self.x * other
            y1 = self.y * other
            z1 = self.z * other
        elif isinstance(other, Point):
            x1 = self.x * other.x
            y1 = self.y * other.y
            z1 = self.z * other.z
        else:
            return None

        return Point(x1, y1, z1)

    def __rmul__(self, other):
        if type(other) == int:
            x1 = self.x * other
            y1 = self.y * other
            z1 = self.z * other
        elif isinstance(other, Point):
            x1 = self.x * other.x
            y1 = self.y * other.y
            z1 = self.z * other.z
        else:
            return None

        return Point(x1, y1, z1)

    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                if self.z == other.z:
                    return True
        return False

    def __getitem__(self, item):
        return (self.x, self.y, self.z)[item]
