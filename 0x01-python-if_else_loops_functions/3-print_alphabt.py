#!/usr/bin/python3

# Loop through ASCII values for lowercase letters from 'a' to 'z'
for k in range(97, 123):
    # Skip printing 'e' and 'q'
    if chr(k) == 'e' or chr(k) == 'q':
        continue
    # Print the current lowercase letter
    print(chr(k), end='')
