#!/usr/bin/python3
for i in range(ord('z'), ord('`'), -1):
    j = i
    if j % 2 != 0:
        zz = i - 32
    else:
        zz = i
    print("{:s}".format(chr(zz)), end="")
