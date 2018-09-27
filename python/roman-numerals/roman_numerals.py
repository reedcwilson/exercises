numerals = tuple(zip(
    [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
    ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
))


def numeral(number):
    result = ''
    for arab, num in numerals:
        quot, number = divmod(number, arab)
        result += num * quot
    return result
