def valid(f):
    return lambda s: all(s) and 2*max(s) < sum(s) and f(s)


@valid
def is_equilateral(sides):
    return len(set(sides)) == 1


@valid
def is_isosceles(sides):
    return len(set(sides)) < 3


@valid
def is_scalene(sides):
    return len(set(sides)) == 3
