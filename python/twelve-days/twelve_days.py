
day = 'On the {} day of Christmas my true love gave to me, '
ths = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
       'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']


def get_gift(i, start):
    gifts = [
        'a Partridge in a Pear Tree', 'two Turtle Doves', 'three French Hens',
        'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying',
        'seven Swans-a-Swimming', 'eight Maids-a-Milking',
        'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping',
        'twelve Drummers Drumming'
    ]
    return 'and {}'.format(gifts[0]) if (i == 0 and start > 1) else gifts[i]


def recite(start, end):
    return [
        '{}{}.'.format(
            day.format(ths[i]),
            ', '.join([get_gift(j-1, i+1) for j in range(i+1, 0, -1)])
        )
        for i in range(start-1, end)
    ]
