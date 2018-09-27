from math import sqrt
from itertools import count, islice


def primes_gen():
    primes = {2}
    yield 2
    for i in count(3, 2):
        candidates = {n for n in primes if n <= sqrt(i)}
        for candidate in candidates:
            if i % candidate == 0:
                break
        else:
            primes.add(i)
            yield i


def nth_prime(n):
    if n < 1:
        raise ValueError('n needs to be greater than 0')
    return next(islice(primes_gen(), n - 1, n))
