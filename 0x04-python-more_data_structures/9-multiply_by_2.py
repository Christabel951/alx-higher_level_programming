#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    product = {}
    for i in a_dictionary:
        product[i] = a_dictionary[i] * 2
    return product
