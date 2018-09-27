from __future__ import division
from fractions import gcd


def op(e, a, b):
    a1, a2, b1, b2 = a.n, a.d, b.n, b.d
    nexp, dexp = e.split(' / ')
    return eval(nexp), eval(dexp)


def reduce(a1, a2):
    if a1 == 0:
        return 0, 1
    com = gcd(a1, a2)
    n, d = a1 // com, a2 // com
    if n > 0 and d < 0:
        return -n, -d
    return n, d


class Rational(object):
    def __init__(self, n, d):
        self.n, self.d = reduce(n, d)

    def __eq__(self, other):
        return self.n == other.n and self.d == other.d

    def __repr__(self):
        return '{}/{}'.format(self.n, self.d)

    def __add__(a, b):
        return Rational(*op("(a1 * b2 + a2 * b1) / (a2 * b2)", a, b))

    def __sub__(a, b):
        return Rational(*op("(a1 * b2 - a2 * b1) / (a2 * b2)", a, b))

    def __mul__(a, b):
        return Rational(*op("(a1 * b1) / (a2 * b2)", a, b))

    def __truediv__(a, b):
        return Rational(*op("(a1 * b2) / (a2 * b1)", a, b))

    def __abs__(a):
        return a if a.n >= 0 else Rational(-a.n, a.d)

    def __pow__(a, n):
        return Rational(eval("a.n ** n"), eval("a.d ** n"))

    def __rpow__(a, n):
        return eval("n ** (a.n / a.d)")
