
def get_multiples(num, limit):
    return [i for i in range(num, limit, num)]


def sum_of_multiples(limit, nums):
    multiples = set(item for m in nums for item in get_multiples(m, limit))
    return sum(multiples)
