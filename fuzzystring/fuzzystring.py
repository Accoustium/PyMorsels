class FuzzyString(str):
    def __init__(self, string: str):
        self.initial_string: str = str(string)

    def __repr__(self):
        return repr(self.initial_string)

    def __str__(self):
        return self.initial_string

    def __eq__(self, other):
        if isinstance(other, FuzzyString):
            return self.initial_string.lower() == other.initial_string.lower()
        elif isinstance(other, str):
            return self.initial_string.lower() == str(other).lower()
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, FuzzyString):
            return self.initial_string.lower() != other.initial_string.lower()
        elif isinstance(other, str):
            return self.initial_string.lower() != str(other).lower()
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, FuzzyString):
            return self.initial_string.lower() > other.initial_string.lower()
        elif isinstance(other, str):
            return self.initial_string.lower() > str(other).lower()
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, FuzzyString):
            return self.initial_string.lower() >= other.initial_string.lower()
        elif isinstance(other, str):
            return self.initial_string.lower() >= str(other).lower()
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, FuzzyString):
            return self.initial_string.lower() < other.initial_string.lower()
        elif isinstance(other, str):
            return self.initial_string.lower() < str(other).lower()
        else:
            return False

    def __le__(self, other):
        if isinstance(other, FuzzyString):
            return self.initial_string.lower() <= other.initial_string.lower()
        elif isinstance(other, str):
            return self.initial_string.lower() <= str(other).lower()

    def __contains__(self, item):
        if isinstance(item, FuzzyString):
            return item.initial_string.lower() in self.initial_string.lower()
        elif isinstance(item, str):
            return str(item).lower() in self.initial_string.lower()

    def __add__(self, other):
        if isinstance(other, FuzzyString):
            return self.initial_string + other.initial_string
        elif isinstance(other, str):
            return FuzzyString(self.initial_string + str(other))
