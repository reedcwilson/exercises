
def sieve(limit):
    nums = [False, False]
    nums.extend([True] * (limit-1))
    primes = []
    for i, is_prime in enumerate(nums):
        if is_prime:
            primes.append(i)
            for n in range(i*i, limit+1, i):
                nums[n] = False
    return primes
