#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        bigger = my_list[0]
        i = 1
        while i < len(my_list):
            if len(my_list) > 1:
                if bigger < my_list[i]:
                    bigger = my_list[i]
            i += 1
        return bigger
