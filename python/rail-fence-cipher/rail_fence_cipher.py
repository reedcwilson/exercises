from itertools import chain, cycle


def idxs(num, size):
    return zip(
            cycle(chain(range(num), range(num-2, 0, -1))),
            range(size)
        )


def encode(msg, num):
    return ''.join(msg[i] for _, i in sorted(idxs(num, len(msg))))


def decode(msg, rails):
    i_map = zip(msg, sorted(idxs(rails, len(msg))))
    return ''.join(c for c, _ in sorted(i_map, key=lambda e: e[1][1]))
