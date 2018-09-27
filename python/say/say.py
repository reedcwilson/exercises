basics = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty'
}

decs = {
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety'
}

TEN = 10
HUNDRED = 100
THOUSAND = 1e3
MILLION = 1e6
BILLION = 1e9
MAX = 1e12 - 1
MIN = 0


def get_amount(number, minimum, string):
    first = trans(number // minimum) + ' ' + string
    rest = number % minimum
    return first if not rest else '{} {}'.format(first, trans(rest, True))


def trans(number, recurse=False):
    if number < 21:
        return basics[number] if not recurse else 'and ' + basics[number]

    if number < HUNDRED:
        if number % TEN == 0:
            return decs[number]
        return '-'.join([decs[int(number / TEN) * TEN], basics[number % TEN]])

    if number < THOUSAND:
        first = basics[number // HUNDRED] + ' hundred'
        rest = number % HUNDRED
        return first if not rest else '{} and {}'.format(first, trans(rest))

    if number < MILLION:
        return get_amount(number, THOUSAND, 'thousand')

    if number < BILLION:
        return get_amount(number, MILLION, 'million')

    return get_amount(number, BILLION, 'billion')


def say(number):
    if number < MIN or number > MAX:
        raise ValueError('Number must be between {} and {}'.format(MIN, MAX))
    return trans(number)
