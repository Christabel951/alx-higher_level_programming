#!/usr/bin/python3
def remove_char_at(str, n):
    dest = ""
    j = 0
    for i in str:
        if j != n:
            dest += i
        j += 1
    return dest
