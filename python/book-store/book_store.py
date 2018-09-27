from itertools import groupby


_discounts = [0, .05, .1, .2, .25]


def take(n, books):
    lst = []
    for i in range(len(books)):
        if len(lst) == n:
            break
        if books[i] == 0:
            continue
        lst.append(True)
        books[i] -= 1
    return lst


def get_scenarios(book_nums):
    scenarios = []
    for group_size in range(1, len(book_nums) + 1):
        scenario = []
        books = book_nums[:]
        while True:
            group = take(group_size, books)
            if not group:
                break
            scenario.append(group)
        scenarios.append(scenario)
    return scenarios


def price_group(group):
    group_len = len(group)
    discount = 1 - _discounts[group_len - 1]
    return 800 * group_len * discount


def calculate_total(books):
    if not books:
        return 0
    book_nums = [len(list(v)) for _, v in groupby(sorted(books))]
    scenarios = get_scenarios(book_nums)
    totals = [sum(price_group(g) for g in s) for s in scenarios]
    return min(totals)
