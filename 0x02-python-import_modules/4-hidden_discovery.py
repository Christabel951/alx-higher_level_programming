#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arrs = dir()
    for i in arrs:
        if i[0:2] != "__":
            print("{}".format(arr[i]))
