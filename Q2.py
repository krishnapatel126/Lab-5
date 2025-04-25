import random

random_integers = [random.randint(1, 100) for _ in range(20)]
print("Generated list of 20 random integers:", random_integers)

user_number = int(input("Enter a number to find its positions in the list: "))
positions = [index for index, value in enumerate(random_integers) if value == user_number]

if positions:
    print(f"The number {user_number} is found at the following position(s): {positions}")
else:
    print(f"The number {user_number} is not found in the list.")
