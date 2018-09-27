

def hey(phrase):
    p = phrase.strip()
    if p == '':
        return 'Fine. Be that way!'
    elif p.isupper():
        return 'Whoa, chill out!'
    elif p.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'
