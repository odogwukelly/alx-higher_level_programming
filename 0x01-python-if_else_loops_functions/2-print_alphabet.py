#!/usr/bin/python3

# Loop through the ASCII values of lowercase letters (97 to 122)
for j in range(97, 123):
    # Convert the ASCII value to its corresponding character
    letter = chr(j)

    # Print the letter without a new line
    print('{}'.format(letter), end='')