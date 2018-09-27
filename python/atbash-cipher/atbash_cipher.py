
import string

cipher = str.maketrans(
    string.ascii_lowercase,
    string.ascii_lowercase[::-1],
    string.whitespace + string.punctuation
)


def encode(plain_text):
    text = plain_text.lower().translate(cipher)
    return ' '.join([text[i:(i+5)] for i in range(0, len(text), 5)])


def decode(cipher_text):
    return cipher_text.translate(cipher)
