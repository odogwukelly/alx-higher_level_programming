 #!/usr/bin/python3
 for p in range(26):
     if p % 2 == 0:
         print('{:c}'.format(122 - p), end='')
     else:
         print('{:c}'.format(90 - p), end='')
