def primitive_triplets(number_in_triplet):
    pass


def triplets_in_range(m, n):
    triplets = set()
    for a in range(m, n + 1):
        for b in range(a + 1, n + 1):
            c = int((a**2 + b**2)**(0.5) + 0.5)
            triplet = (a, b, c)
            if is_triplet(triplet) and m <= c <= n:
                triplets.update([triplet])
    return triplets


def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2
