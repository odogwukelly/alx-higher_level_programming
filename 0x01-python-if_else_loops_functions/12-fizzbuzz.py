#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

def fizzbuzz():
    # Iterate over numbers from 1 to 100
    for number in range(1, 101):
        # Check if the number is divisible by both 3 and 5
        if number % 5 == 0 and number % 3 == 0:
            print('FizzBuzz', end=' ')  # If divisible by both, print 'FizzBuzz'
        # Check if the number is divisible by 5
        elif number % 5 == 0:
            print('Buzz', end=' ')  # If divisible by 5, print 'Buzz'
        # Check if the number is divisible by 3
        elif number % 3 == 0:
            print('Fizz', end=' ')  # If divisible by 3, print 'Fizz'
        else:
            print(number, end=' ')  # If not divisible by either, print the number itself

