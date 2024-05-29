#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

# Outer loop through numbers from 0 to 9 (inclusive)
for k in range(0, 10):
    # Inner loop through numbers from k+1 to 9 (inclusive)
    for j in range(k + 1, 10):
        # Check if the current pair is (8, 9)
        if k == 8 and j == 9:
            # Print the pair without a trailing comma and space
            print('{:d}{:d}'.format(k, j))
        else:
            # Print the pair followed by a comma and space
            print('{}{}'.format(k, j), end=', ')

