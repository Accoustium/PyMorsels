def tail(seq, right):
    if right > 0:
        __seq = [x for x in seq]
        if right > len(__seq):
            right = len(__seq)

        return __seq[(len(__seq) - right):]
    else:
        return []