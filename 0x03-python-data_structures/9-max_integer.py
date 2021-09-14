#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        bigger = 0
        i = 0
        while i < len(my_list) - 1:
            if len(my_list) == 1:
                return my_list[i]
            else:
                if my_list[i] < my_list[i + 1]:
                    if bigger < my_list[i + 1]:
                        bigger = my_list[i + 1]
                i += 1
        return bigger
