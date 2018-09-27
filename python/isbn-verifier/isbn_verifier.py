

def is_isbn(isbn):
    nums = [int(n) if n != 'X' else 10 for n in isbn]
    return sum([x * i for x, i in zip(nums, range(10, 0, -1))]) % 11 == 0


def valid_digits(isbn):
    c = isbn[9]
    return all([d.isdigit() for d in isbn[0:9]]) and (c.isdigit() or c == 'X')


def verify(isbn):
    isbn = isbn.replace('-', '').upper()
    return len(isbn) == 10 and valid_digits(isbn) and is_isbn(isbn)
