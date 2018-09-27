from random import randrange as rand


class Cipher(object):
    def __init__(self, key=None):
        if key:
            self._ensure_valid(key)
            key_len = len(key)
            self.__key = key * (100 // key_len) if key_len < 100 else key
        else:
            self.__key = ''.join(chr(rand(26) + ord('a')) for _ in range(100))
        self.__dist = [ord(c) - ord('a') for c in self.__key]

    def _ensure_valid(self, key):
        for c in key:
            if not c.isalpha() or not c.islower():
                raise ValueError('key must only include lowercase alpha chars')

    def _sanitize(self, text):
        return ''.join(c for c in text.lower() if c.isalpha())

    def _transform(self, c, d, shift_func):
        return chr(shift_func(ord(c) - ord('a'), d) % 26 + ord('a'))

    def _code(self, text, shift_func):
        return ''.join(
                    self._transform(c, d, shift_func)
                    for d, c in zip(self.__dist, self._sanitize(text))
                )

    def encode(self, text):
        return self._code(text, lambda a, b: a + b)

    def decode(self, text):
        return self._code(text, lambda a, b: a - b)

    @property
    def key(self):
        return self.__key


class Caesar(Cipher):
    def __init__(self):
        super().__init__('d' * 100)
