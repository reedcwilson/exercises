
braces = {'[': ']', '(': ')', '{': '}'}


def is_paired(input_string):
    b = []
    for c in input_string:
        if c in braces:
            b.append(braces[c])
        elif c in braces.values():
            if len(b) == 0 or c != b.pop():
                return False
    return len(b) == 0
