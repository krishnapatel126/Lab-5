import random

random_numbers = [random.randint(-100, 100) for _ in range(30)]
print("Generated list of 30 random numbers:", random_numbers)

positive_numbers = [num for num in random_numbers if num > 0]
negative_numbers = [num for num in random_numbers if num < 0]

print("List of positive numbers:", positive_numbers)
print("List of negative numbers:", negative_numbers)
