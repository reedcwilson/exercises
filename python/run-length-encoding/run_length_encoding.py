from itertools import groupby


def decode(string):
    new = ''
    num = ''
    for c in string:
        if c.isdigit():
            num += c
            continue
        new += c * (int(num) if num != '' else 1)
        num = ''
    return new


def encode(string):
    new = ''
    groups = [list(g) for k, g in groupby(string)]
    for group in groups:
        if len(group) > 1:
            new += str(len(group))
        new += group[0] if len(group) > 0 else ''
    return new


if __name__ == '__main__':
    print(decode(encode('AADBBBCCCC')))
