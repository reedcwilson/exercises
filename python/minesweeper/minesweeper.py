adj = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == y == 0)]


def distance(field, x, y):
    if field[y][x] == '*':
        return '*'
    d = 0
    for dx, dy in adj:
        if 0 <= (x+dx) < len(field[0]) and 0 <= (y+dy) < len(field):
            if field[y+dy][x+dx] == '*':
                d += 1
    return str(d) if d != 0 else ' '


def ensure(field):
    if not all(len(field[0]) == len(r) for r in field):
        raise ValueError('The field must be regular')
    if any(c != '*' and c != ' ' for r in field for c in r):
        raise ValueError('Only "*" or " " characters are allowed')


def board(field):
    ensure(field)
    return [''.join([distance(field, x, y) for x, _ in enumerate(r)])
            for y, r in enumerate(field)]
