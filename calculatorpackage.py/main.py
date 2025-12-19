import add,sub,division,multiply

print("----- Registry Based Calculator -----")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operations = {
    add.get_operation(): add.calculate,
    sub.get_operation(): sub.calculate,
    multiply.get_operation(): multiply.calculate,
    division.get_operation(): division.calculate
}

print("\nResults:")
for name, func in operations.items():
    print(f"{name}: {func(a, b)}")