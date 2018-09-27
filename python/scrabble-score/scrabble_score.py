
letters = {
    l: s
    for s, letters in {
        1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'],
        2: ['d', 'g'],
        3: ['b', 'c', 'm', 'p'],
        4: ['f', 'h', 'v', 'w', 'y'],
        5: ['k'],
        8: ['j', 'x'],
        10: ['q', 'z'],
    }.items()
    for l in letters
}


def score(word):
    return sum(letters[c] for c in word.lower())
