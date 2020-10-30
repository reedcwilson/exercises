# Given a string that consists of only two types of characters: '(' and ')',
# balance the parentheses by inserting either a '(' or a ')' as many times as
# necessary. Determine the minimum number of characters that must be inserted.


def getMin(s):
    return abs(sum(1 if c == '(' else -1 for c in s if c == '(' or c == ')'))
