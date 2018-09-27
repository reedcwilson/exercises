
def is_vowel(c):
    return 'aeiou'.count(c) > 0


def qu_rule(word, c, i):
    return c == 'u' and i > 0 and word[i-1] == 'q'


def y_rule(word, c, i):
    return i == 0 and c == 'y' and len(word) > 1 and not is_vowel(word[i + 1])


def cluster_rule(consonants, c):
    return consonants > 1 and c == 'y'


def x_rule(word, c, i):
    return i == 0 and c == 'x' and len(word) > 1 and not is_vowel(word[i + 1])


def get_split(w):
    consonants = 0
    for i, c in enumerate(w):
        if (
                is_vowel(c) or
                y_rule(w, c, i) or
                cluster_rule(consonants, c) or
                x_rule(w, c, i)
        ):
            if qu_rule(w, c, i):
                continue
            return i
        else:
            consonants += 1
    return -1


def translate(text):
    words = text.split()
    for i, w in enumerate(words):
        vowel_idx = get_split(w)
        words[i] = '{}{}ay'.format(w[vowel_idx:], w[:vowel_idx])
    return ' '.join(words)
