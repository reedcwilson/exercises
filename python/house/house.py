
_p = [
    ('that lay in', 'the house that Jack built.'),
    ('that ate', 'the malt'),
    ('that killed', 'the rat'),
    ('that worried', 'the cat'),
    ('that tossed', 'the dog'),
    ('that milked', 'the cow with the crumpled horn'),
    ('that kissed', 'the maiden all forlorn'),
    ('that married', 'the man all tattered and torn'),
    ('that woke', 'the priest all shaven and shorn'),
    ('that kept', 'the rooster that crowed in the morn'),
    ('that belonged to', 'the farmer sowing his corn'),
    ('', 'the horse and the hound and the horn')
]


def _get_verse(n):
    v = ['This is {}'.format(_p[n][1])]
    v.extend(['{} {}'.format(_p[i][0], _p[i][1]) for i in range(n-1, -1, -1)])
    return v


def recite(start_verse, end_verse):
    rhyme = []
    for i in range(start_verse-1, end_verse):
        rhyme.extend(_get_verse(i))
        rhyme.append("")
    return rhyme[0:-1]
