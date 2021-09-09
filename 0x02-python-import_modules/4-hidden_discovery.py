#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    ar = dir()
    for i in range(0, len(ar)):
        if ar[i][0:2] != "__":
            print("{}".format(ar[i]))
