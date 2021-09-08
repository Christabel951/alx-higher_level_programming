#!/usr/bin/python3
for i in range(ord('A'), ord('Z') + 1):
    if chr(i) == 'Z':
        print(chr(i))
    else:
        print(chr(i), end=" ")
