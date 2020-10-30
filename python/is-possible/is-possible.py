
# Consider a pair of integers, (a, b). The following operations can be
# performed on (a, b) in any order, zero or more times:
#
# (a, b) → (a + b, b)
# (a, b) → (a, a + b)
#
# For example, starting with (1, 1), perform the operation (1, 1 + 1) to get
# (1, 2), perform the operation (1 + 2, 2) to get (3, 2), and perform the
# operation (3+2, 2) to get (5, 2). Alternatively, the first operation could be
# (1+1, 1) to get (2, 1) and so on. The diagram below demonstrates the example
# representing the pairs as Cartesian coordinates:
#
#
# Function Description
# Complete the function isPossible in the editor below. The function must
# return a string that denotes whether or not you can convert (a, b) to (c, d)
# by performing zero or more of the operations specified above. If it is
# possible, return the string Yes. Otherwise, return No.
#
# isPossible has the following parameter(s):
#     a:  an integer
#     b:  an integer
#     c:  an integer
#     d:  an integer
#
# Constraints
# 1 ≤ a, b, c, d ≤ 1000
#
# Sample Input
# 1
# 4
# 5
# 9
#
# Sample Output
# Yes

import sys

sys.setrecursionlimit(1004)


def isPossible(a, b, c, d):
    return 'Yes' if is_possible(a, b, c, d) else 'No'


def is_possible(a, b, c, d):
    if a > c or b > d:
        return False
    if a == c and b == d:
        return True
    return is_possible(a, a + b, c, d) or is_possible(a + b, b, c, d)
