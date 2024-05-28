#!/usr/bin/python3

# Import the random module
import random

# Generate a random integer between -10000 and 10000
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
lastNum = abs(number) % 10

# Check if the number is greater than 5
if number > 5:
    print(f'Last digit of {number} is {lastNum} and is greater than 5')

# Check if the number is equal to 0
elif number == 0:
    print(f'Last digit of {number} is {lastNum} and is 0')

# If the number is not greater than 5 and not equal to 0
else:
    print(f'Last digit of {number} is -{lastNum} and is less than 6 and not 0')