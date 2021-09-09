#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv)
    ac -= 1
    sum1 = 0
    if ac == 0:
        print("{}".format(sum1))
    else:
        for i in sys.argv[1:]:
            sum1 += int(i)
        print("{}".format(sum1))
