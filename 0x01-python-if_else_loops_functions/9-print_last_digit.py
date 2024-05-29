#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

def print_last_digit(number):
    # Compute the absolute value of the number and then get the last digit
    k = abs(number) % 10
    # Print the last digit without a newline
    print(f"{k}", end='')
    # Return the last digit
    return k

