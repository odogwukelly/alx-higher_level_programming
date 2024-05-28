#!/usr/bin/python3

# A script that print random numbers and check if positive, negative or zero
import random
number = random.randint(-10, 10)
if number > 0:
    print(f'{number:d} is positive')
elif number == 0:
    print(f'{number:d} is zero')
else:
    print(f'{number:d} is negative')
