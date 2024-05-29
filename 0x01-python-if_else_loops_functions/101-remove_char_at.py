#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

def remove_char_at(string, n):
    # Create a new string by concatenating the substring before the character at index 'n'
    # with the substring after the character at index 'n'
    x = string[:n] + string[n + 1:]

    # Check if 'n' is negative (i.e., attempting to remove a character beyond the end of the string)
    if n < 0:
        # If 'n' is negative, return the original string unchanged
        return string

    # If 'n' is a valid index, return the modified string
    return x


