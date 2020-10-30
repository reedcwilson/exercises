def convert(n):
    v = [f'Pl{l}ng' for f, l in {3: 'i', 5: 'a', 7: 'o'}.items() if not n % f]
    return str(n) if not v else ''.join(v)
