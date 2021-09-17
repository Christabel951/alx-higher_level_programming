#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avg = 0
    div = 0
    for tupl in my_list:
        avg += tupl[0] * tupl[1]
        div += tupl[1]
    return float(avg / div)
