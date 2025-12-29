def calculator(func):
    def wrapper(a, b):
        return a + b
    return wrapper


@calculator
def add(a, b):
    pass


print(add(15, 25))
