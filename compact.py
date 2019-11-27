def compact(param):
    try:
        if type(param) != list:
            return param
        value = []
        for k, v in enumerate(param):
            if k > 0:
                if param[k - 1] != v:
                    value.append(v)
            else:
                value.append(v)

        return value

    except TypeError:
        return None
