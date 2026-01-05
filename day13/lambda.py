numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
