__codes = ['wink', 'double blink', 'close your eyes', 'jump']


def handshake(code):
    codes = [__codes[i] for i in range(len(__codes)) if 1 << i & code != 0]
    return codes if code & 1 << 4 == 0 else codes[::-1]


def secret_code(actions):
    c = [__codes.index(c) for c in actions]
    if len(c) > 1 and sorted(c, reverse=True) == c:
        c.append(len(__codes))
    return sum(1 << n for n in c)
