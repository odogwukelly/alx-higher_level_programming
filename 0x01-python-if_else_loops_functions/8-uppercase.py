#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

def uppercase(string):
    # Iterate over each character in the input string
    for upper in string:
        # Check if the character is a lowercase letter (ASCII value between 97 and 122)
        if 97 <= ord(upper) <= 122:
            # Convert the character to uppercase by subtracting 32 from its ASCII value
            upper = chr(ord(upper) - 32)
        # Print the character without a newline, staying on the same line
        print("{:s}".format(upper), end='')

    # Print a newline character at the end
    print('\n', end="")

