def ensure_valid_square(func):
    def wrapper(num):
        if not 0 < num <= 64:
            raise ValueError("valid input: 1 - 64")
        return func(num)
    return wrapper


@ensure_valid_square
def on_square(num):
    return 2**(num-1)


@ensure_valid_square
def total_after(num):
    return 2**num - 1
