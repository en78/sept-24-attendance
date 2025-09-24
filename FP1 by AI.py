import random
import time

# Get the user's name
varUserName = input("Hello! What's your name? ")

# Greet the user by name
print(f"Nice to meet you, {varUserName}!")

# Generate and display random numbers
print("Here are some random numbers for you:")

# Generate numbers for the powerball
time.sleep(.5)
num1 = random.randint(1, 69)
num2 = random.randint(1, 69)
num3 = random.randint(1, 69)
num4 = random.randint(1, 69)
num5 = random.randint(1, 69)
num6 = random.randint(1, 26)

# Print the numbers with specific spacing
print(f"{num1}  {num2}  {num3}  {num4}  {num5}    {num6}")

# Farewell message
print("Have a great day!")