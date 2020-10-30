key = ['black', 'brown', 'red', 'orange', 'yellow',
       'green', 'blue', 'violet', 'grey', 'white']


def value(colors):
    return int(''.join(str(key.index(c)) for c in colors))
