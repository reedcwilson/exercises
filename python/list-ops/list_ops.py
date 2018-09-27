def append(xs, ys):
    return concat([xs, ys])


def concat(lists):
    return [e for s in lists for e in s]


def filter_clone(f, xs):
    return [e for e in xs if f(e)]


def length(xs):
    return sum(1 for e in xs)


def map_clone(f, xs):
    return [f(e) for e in xs]


def foldl(f, xs, acc):
    return acc if length(xs) == 0 else foldl(f, xs[1:], f(acc, xs[0]))


def foldr(f, xs, acc):
    return acc if length(xs) == 0 else f(xs[0], foldr(f, xs[1:], acc))


def reverse(xs):
    return xs[::-1]
