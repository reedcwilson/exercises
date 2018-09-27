from itertools import zip_longest as zip


def transpose(input_lines):
    return '\n'.join([
        ''.join(t).rstrip()
        for t in
        zip(*input_lines.replace(' ', '_').splitlines(), fillvalue=' ')
    ]).strip().replace('_', ' ')
