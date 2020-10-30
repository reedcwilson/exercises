def reversed_args(f):
    def wrapper(*args):
        return f(*args[::-1])
    return wrapper
