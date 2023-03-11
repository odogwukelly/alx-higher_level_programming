#!/usr/bin/python3
for ken in range(0, 8):
    for j in range(ken + 1, 10):
        print('{:d}{:d}'.format(ken, j),end=', ')
print('{:d}{:d}'.format(ken + 1, j)) 
