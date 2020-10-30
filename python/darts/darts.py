def score(x, y):
    config = ((1, 10), (5, 5), (10, 1))
    for r, p in config:
        if sum([c**2 for c in (x, y)]) <= r**2:
            return p
    return 0
