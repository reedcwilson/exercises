from functools import reduce
from operator import mul


def largest_product(series, size):
    if size < 0:
        raise ValueError('Size must be positive: {}'.format(size))
    combos = [list(series[i:i+size]) for i in range(len(series)-size+1)]
    return max(reduce(mul, map(int, c), 1) for c in combos)
