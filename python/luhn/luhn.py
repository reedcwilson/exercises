class Luhn(object):
    def __init__(self, c):
        c = c.replace(' ', '')[::-1]
        if not c.isdigit() or len(c) < 2:
            self.__valid = False
            return
        inc = (n if i % 2 == 0 else n * 2 for i, n in enumerate(map(int, c)))
        self.__valid = sum(n if n < 10 else n - 9 for n in inc) % 10 == 0

    def is_valid(self):
        return self.__valid
