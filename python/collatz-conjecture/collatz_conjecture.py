def steps(n, times=0):
    if n < 1:
        raise ValueError('number must be positive')
    if n == 1:
        return times
    return steps((n//2) if not (n%2) else (n*3+1), times+1)
