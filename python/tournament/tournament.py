def tally(results):
    t = {}
    for line in results.split('\n'):
        if not line:
            return tablify({})
        h, a, r = line.split(';')
        t[h] = '{}{}'.format(
            t.get(h, ''),
            'w' if r == 'win' else 'l' if r == 'loss' else 'd'
        )
        t[a] = '{}{}'.format(
            t.get(a, ''),
            'l' if r == 'win' else 'w' if r == 'loss' else 'd'
        )
    return tablify(t)


def tablify(results):
    table = []
    for team, r in results.items():
        table.append((
            team.ljust(31),
            len(r),
            sum(1 for x in r if x == 'w'),
            sum(1 for x in r if x == 'd'),
            sum(1 for x in r if x == 'l'),
            sum(3 if x == 'w' else 1 if x == 'd' else 0 for x in r),
        ))
    string = 'Team                           | MP |  W |  D |  L |  P'
    table.sort(key=lambda x: x[0])
    for item in sorted(table, key=lambda x: x[5], reverse=True):
        string += '\n{}|  {} |  {} |  {} |  {} |  {}'.format(*item)
    return string
