
def get_counts(word):
    letters = {}
    for letter in word:
        l = letter.lower()
        letters[l] = letters.get(l, 0) + 1
    return letters


def detect_anagrams(word, candidates):
    word_counts = get_counts(word)
    return [c for c in candidates
            if word.lower() != c.lower() and word_counts == get_counts(c)]
