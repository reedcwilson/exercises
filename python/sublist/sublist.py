SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 0, 1, 2, 3


def check_lists(a, b):
    def is_sub(a, b):
        c, d = len(a), len(b)
        return c > d and any(a[i:i+d] == b for i in range(c))
    return (EQUAL if a == b else
            SUBLIST if is_sub(b, a) else
            SUPERLIST if is_sub(a, b) else
            UNEQUAL)
