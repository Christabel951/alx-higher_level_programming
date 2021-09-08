#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            fzbz = "FizzBuzz"
        elif i % 5 == 0:
            fzbz = "Buzz"
        elif i % 3 == 0:
            fzbz = "Fizz"
        else:
            fzbz = i
        print("{}".format(fzbz), end=" ")
