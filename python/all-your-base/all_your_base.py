def _from(base, digits):
    return sum(d * base**i for i, d in enumerate(digits[::-1]))


def _to(base, num):
    nums = []
    while num > 0:
        num, m = divmod(num, base)
        nums.append(m)
    return nums[::-1]


def rebase(a, digits, b):
    if (a < 2 or b < 2):
        raise ValueError('base must be greater than 1')
    if any(d < 0 or d >= a for d in digits):
        raise ValueError('digits must be positive and less than original base')
    return _to(b, _from(a, digits))
