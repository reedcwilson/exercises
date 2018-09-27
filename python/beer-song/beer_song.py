def beer_num(num):
    bottles = 'bottles'
    if num == 1:
        bottles = 'bottle'
    if num == 0:
        num = 'no more'
    return '{} {} of beer'.format(num, bottles)


def on_the_wall(num):
    return '{} on the wall'.format(beer_num(num))


def take_one(num):
    article = 'one'
    if num == 1:
        article = 'it'
    return 'Take {} down and pass it around, {}.'.format(
            article,
            on_the_wall(num - 1))


def no_more():
    return [
        "No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, 99 bottles of beer on the wall."
    ]


def recite(start, take=1):
    song = []
    for i in range(start, start - take, -1):
        if i == 0:
            song.extend(no_more())
            break
        song.append('{}, {}.'.format(on_the_wall(i), beer_num(i)))
        song.append('{}'.format(take_one(i)))
        song.append('')
    if song[-1] == '':
        return song[:-1]
    return song
