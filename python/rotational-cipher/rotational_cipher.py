import string


def rotate(text, key):
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    cipher = []
    for c in text:
        if c.isalpha():
            alphabet = uppercase if c.isupper() else lowercase
            cipher.append(alphabet[(alphabet.index(c) + key) % len(alphabet)])
        else:
            cipher.append(c)
    return ''.join(cipher)
