#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

# Loop through numbers from 0 to 25 (inclusive)
for i in range(26):
    # Check if the current number is even
    if i % 2 == 0:
        # Print a character corresponding to the ASCII value of (122 - i), which goes from 'z' to 'a'
        print('{:c}'.format(122 - i), end=' ')
    else:
        # Print a character corresponding to the ASCII value of (90 - i), which goes from 'Z' to 'A'
        print('{:c}'.format(90 - i), end=' ')

