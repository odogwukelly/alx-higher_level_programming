#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    # Check if 'a' is less than 'b'
    if a < b:
        return c  # If 'a' is less than 'b', return 'c'

    # Check if 'c' is greater than 'b'
    if c > b:
        return a + b  # If 'c' is greater than 'b', return the sum of 'a' and 'b'

    # If none of the above conditions are met, return the result of the expression 'a * b - c'
    return a * b - c

