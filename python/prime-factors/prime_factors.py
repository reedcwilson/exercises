def prime_factors(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i == 0:
            factors.append(i)
            num //= i
        else:
            i += 1
    if num > 1:
        factors.append(num)
    return factors
