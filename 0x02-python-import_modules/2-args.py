#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv)
    ac -= 1
    if ac == 0:
        print("{} arguments.".format(ac))
    elif ac == 1:
        print("{} argument:".format(ac))
    else:
        print("{} arguments:".format(ac))
    j = 1
    if ac >= j:
        for i in sys.argv[1:]:
            print("{}: {}".format(j, i))
            j += 1
