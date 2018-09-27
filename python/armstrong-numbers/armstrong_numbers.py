def is_armstrong(number):
    return number == sum(int(n)**len(str(number)) for n in str(number))
