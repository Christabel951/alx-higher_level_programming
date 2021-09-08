#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    unum = number * -1
else:
    unum = number
last_d = unum % 10
if number < 0:
    last_d *= -1
if last_d > 5:
    str = "and is greater than 5"
elif last_d == 0:
    str = "and is 0"
elif last_d < 6 and not 0:
    str = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, last_d, str))
