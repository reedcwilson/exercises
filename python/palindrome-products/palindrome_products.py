
# def is_palindrome(string):
#     return string == string[::-1]


# def get_palindromes(a, b):
#     nums = list(range(a, b+1))
#     return {
#         a * b: (a, b)
#         for a in nums
#         for b in nums
#         if is_palindrome(str(a * b))
#     }


# def largest_palindrome(max_factor, min_factor=0):
#     p = get_palindromes(min_factor, max_factor)
#     k = max(p, key=p.get)
#     return k, {p[k]}


# def smallest_palindrome(max_factor, min_factor=0):
#     p = get_palindromes(min_factor, max_factor)
#     k = min(p, key=p.get)
#     return k, {p[k]}

def _palindrome(max_factor, min_factor, op):
    xs = [(x * y, (x, y))
        for x in range(min_factor, max_factor + 1)
        for y in range(x, max_factor + 1)
        for s in [str(x * y)]
        if s == s[::-1]]

    a, b = op(xs)
    return (a, { q for p, q in xs if p == a })


def largest_palindrome(max_factor, min_factor):
    return _palindrome(max_factor, min_factor, max)


def smallest_palindrome(max_factor, min_factor):
    return _palindrome(max_factor, min_factor, min)

