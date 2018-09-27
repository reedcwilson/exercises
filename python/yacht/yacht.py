def _get_counts(s):
    return zip(*sorted(((s.count(i), i) for i in set(s)), reverse=True))


def _full_house(s):
    c, n = _get_counts(s)
    return sum(a * b for a, b in zip(c, n)) if c == (3, 2) else 0


def _four_of_a_kind(s):
    c, n = _get_counts(s)
    return 4 * n[0] if c[0] >= 4 else 0


def _straight(big=False):
    def f(s):
        c, n = _get_counts(s)
        return 30 if (
            (len(c) == 5 and max(n) - min(n) == 4) and
            (big and n[-1] == 2 or not big and n[-1] == 1)
        ) else 0
    return f


def _count(n):
    return lambda s: n * sum(1 for i in s if i == n)


def _yacht(s):
    return 50 if len(set(s)) == 1 else 0


def _choice(s):
    return sum(i for i in s)


YACHT = _yacht
ONES = _count(1)
TWOS = _count(2)
THREES = _count(3)
FOURS = _count(4)
FIVES = _count(5)
SIXES = _count(6)
CHOICE = _choice
FULL_HOUSE = _full_house
FOUR_OF_A_KIND = _four_of_a_kind
LITTLE_STRAIGHT = _straight(False)
BIG_STRAIGHT = _straight(True)


def score(dice, category):
    return category(dice)
