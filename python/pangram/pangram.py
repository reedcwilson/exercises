
import string


def is_pangram(sentence):
    chars = [c.lower() for c in sentence if c.isalpha()]
    return len(set(chars)) == len(string.ascii_lowercase)


def is_pangram_homemade(sentence):
    chars = [c.lower() for c in sentence if c.isalpha()]
    alphabet = [chr(l) for l in range(97, 123)]
    return len(set(chars)) == len(alphabet)


def is_pangram_hardcode(sentence):
    chars = [c.lower() for c in sentence if c.isalpha()]
    return len(set(chars)) == 26


if __name__ == '__main__':
    print(is_pangram_homemade('The quick brown fox jumps over the lazy dog'))
