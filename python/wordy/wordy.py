from re import split
from operator import floordiv, add, sub, mul

ops_str = ['plus', 'minus', 'multiplied by', 'divided by']
ops = dict(zip(ops_str, [add, sub, mul, floordiv]))


def _get_part(p):
    if p.lstrip('-').isdigit():
        return int(p)
    elif p in ops_str:
        return ops[p]
    else:
        raise ValueError('Unrecognized part:{}'.format(p))


def calculate(question):
    parts = [
        _get_part(p.strip()) for p in
        split(r'(\-?\d+)', question[len('What is'):-1].strip())
        if p
    ]
    num = parts[0]
    pairs = [(parts[i+1], parts[i+2]) for i in range(0, len(parts)-1, 2)]
    for op, n in pairs:
        num = op(num, n)
    return num
