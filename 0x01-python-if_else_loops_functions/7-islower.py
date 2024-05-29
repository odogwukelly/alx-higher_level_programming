#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

def islower(c):
    # Check if the ASCII value of the character is between 97 ('a') and 122 ('z') inclusive
    if 97 <= ord(c) <= 122:
        return True  # Return True if the character is a lowercase letter
    else:
        return False  # Return False otherwise

