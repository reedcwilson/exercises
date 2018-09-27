import argparse
from shlex import split as shplit


def get_args(flags):
    p = argparse.ArgumentParser()
    for c in 'nlivx':
        p.add_argument(f'-{c}', action='store_true')
    return p.parse_args(shplit(flags))


def should_include(line, pattern, args):
    if args.i:
        line = line.lower()
        pattern = pattern.lower()
    if args.x:
        if len(line.rstrip()) != len(pattern):
            return False
    if args.v:
        return pattern not in line
    return pattern in line


def get_matches(matches, files, args):
    result = []
    for line, i, filename in matches:
        if args.l:
            name = f'{filename}\n'
            if name not in result:
                result.append(name)
        else:
            new_line = ''
            if len(files) > 1:
                new_line += f'{filename}:'
            if args.n:
                new_line += f'{i+1}:'
            new_line += line
            result.append(new_line)
    return ''.join(result)


def grep(pattern, files, flags=''):
    args = get_args(flags)
    matches = []
    for filename in files:
        with open(filename, 'r') as f:
            for i, line in enumerate(f.readlines()):
                if should_include(line, pattern, args):
                    matches.append((line, i, filename))
    return get_matches(matches, files, args)
