from string import ascii_uppercase as UP


def get_top(width, height):
    d = []
    for n in range(height):
        row = [' '] * width
        row[height - n - 1] = UP[n]
        row[height + n - 1] = UP[n]
        d.append(row)
    return d


def stringify(diamond):
    return ''.join('{}\n'.format(''.join(r)) for r in diamond)


def make_diamond(letter):
    idx = UP.index(letter) + 1
    top = get_top(idx * 2 - 1, idx)
    return '{}{}'.format(stringify(top[:-1]), stringify(top[::-1]))
