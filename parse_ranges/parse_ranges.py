def int_convert(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        return None


def generate(first: int, second: int):
    for x in range(first, second + 1):
        yield x


def parse_ranges(ranges: str) -> iter:
    total_range = []
    ranges = ranges.split(",")
    for rang in ranges:
        rang = rang.replace(" ", "")
        if rang.find("-") != -1:
            first = int_convert(rang.split("-")[0])
            second = int_convert(rang.split("-")[1])
            if second:
                if first:
                    if first < second:
                        for val in range(first, second + 1):
                            yield val
                    else:
                        yield first
                else:
                    yield second
            else:
                yield first
        else:
            rang = int_convert(rang)
            if rang is not None:
                yield rang
