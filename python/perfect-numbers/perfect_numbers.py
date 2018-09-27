def classify(n):
    if n < 1:
        raise ValueError('number must be positive')
    c = sum(set(e
                for i in range(1, int(pow(n, 0.5) + 1))
                for e in [i, n//i]
                if n % i == 0)) - n
    return 'perfect' if c == n else 'abundant' if c > n else 'deficient'
