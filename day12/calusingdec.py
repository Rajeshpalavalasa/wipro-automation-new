def calculator(func):
    def wrapper():
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if func.__name__ == "add":
            return a + b
        elif func.__name__ == "subtract":
            return a - b
        elif func.__name__ == "divide":
            if b == 0:
                return "Division by zero not allowed"
            return a / b
    return wrapper
@calculator
def add():
    pass

@calculator
def subtract():
    pass

@calculator
def divide():
    pass


print("Addition:", add())
print("Subtraction:", subtract())
print("Division:", divide())
