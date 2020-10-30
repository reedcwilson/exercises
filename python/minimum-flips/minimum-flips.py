from termcolor import colored


def flip(string, start=0):
    chars = [c for c in string]
    for i in range(start, len(string)):
        chars[i] = '0' if chars[i] == '1' else '0'
    return ''.join(chars)


def theFinalProblem(string):
    flips = 0
    for i, c in enumerate(string):
        if c != '0':
            string = flip(string, i)
            flips += 1
    return flips


result_colors = {
    True: 'green',
    False: 'red',
}

if __name__ == '__main__':
    testcases = [
        ['0011', 1],
        ['01011', 3],
    ]
    for string, expected in testcases:
        actual = theFinalProblem(string)
        print(colored(
            f'{string}\t expected: {expected}\t actual: {actual}',
            result_colors[expected == actual]
        ))
