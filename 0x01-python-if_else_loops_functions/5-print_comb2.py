#!/usr/bin/python3  # Shebang line to indicate that the script should be run with Python 3

# Loop through numbers from 0 to 98 (inclusive)
for k in range(0, 99):
    # Print each number formatted as a two-digit number, followed by a comma and a space
    print('{:02d}'.format(k), end=', ')

# Print the number 99 (k + 1) formatted as a two-digit number, without a trailing comma
print('{:02d}'.format(k + 1))


