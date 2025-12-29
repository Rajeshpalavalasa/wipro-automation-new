def star_decorator(func):
    def wrapper():
        return "*****" + func() + "*****"
    return wrapper
@star_decorator
def say_hello():
    return "Hello"

print(say_hello())
def calculator(func):
    def wrapper(a, b):
        result = func(a, b)
        print("Result:", result)
        return result
    return wrapper
@calculator
def add(a, b):
    return a + b

@calculator
def subtract(a, b):
    return a - b


add(11, 22)
subtract(11, 5)
