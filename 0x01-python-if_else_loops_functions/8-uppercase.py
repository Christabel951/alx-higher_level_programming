#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            upper = chr(ord(i) - 32)
        else:
            upper = i
        print("{:s}".format(upper), end="")
    print()
