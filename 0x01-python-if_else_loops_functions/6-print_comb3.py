#!/usr/bin/python3
for ken in range(0, 8):
    for j in range(ken + 1, 10):
        if ken == 8 and j == 9:
            continue
        print('{:d}{:d}'.format(ken, j),end=', ')
