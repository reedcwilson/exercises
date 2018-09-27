from threading import RLock


class BankAccount(object):
    def __init__(self):
        self._balance = 0
        self._is_open = False
        self._lock = RLock()
        self._validations = {
            "open": lambda s, a, k: not s._is_open,
            "amount": lambda s, a, k: a[0] < 0,
            "sufficient": lambda s, a, k: a[0] > s._balance
        }

    def _validate(opts):
        def decorator(func):
            def inner(self, *args, **kwargs):
                for o in opts:
                    if self._validations[o](self, args, kwargs):
                        raise ValueError
                return func(self, *args, **kwargs)
            return inner
        return decorator

    def open(self):
        self._is_open = True

    def close(self):
        self._is_open = False

    @_validate(["open"])
    def get_balance(self):
        with self._lock:
            return self._balance

    @_validate(["open", "amount"])
    def deposit(self, amount):
        with self._lock:
            self._balance += amount

    @_validate(["open", "amount", "sufficient"])
    def withdraw(self, amount):
        with self._lock:
            self._balance -= amount
