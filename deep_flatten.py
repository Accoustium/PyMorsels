def deep_flatten(iterable: list):
    output = []
    for item in iterable:
        if type(item) == int or type(item) == str:
            output.append(item)
        else:
            output.extend(deep_flatten(item))

    return output