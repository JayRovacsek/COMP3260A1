#!/usr/bin/python
import traceback
import sys

def calculate_GCD(i,j,oldi=None,oldj=None):

    if i == j:
        print("Error: Numbers are the same; {}, {}".format(i,j))
    else:
        if i > j:
            prefix = int(i / j)
            remainder = i % j
            greater = i
            lesser = j
        else:
            prefix = int(i / j)
            remainder = j % i
            greater = j
            lesser = i

        print("{}={}({})+{}".format(greater,prefix,lesser,remainder))
        if oldi is None:
            oldi = greater
            oldj = lesser
        if remainder is 0:
            print("Initial inputs; {},{}".format(oldi,oldj))
            print("Found a solution; lowest GCD = {}".format(lesser))
        else:
            calculate_GCD(lesser,remainder,oldi,oldj)

if __name__ == "__main__":
    try:
        if len(sys.argv) is 1:
            i = input("Enter first number:")
            j = input("Enter second number:")
            calculate_GCD(int(i),int(j))
        else:
            args = sys.argv
            del args[0]
            print(args[0],args[1])
            calculate_GCD(int(args[0]),int(args[1]))
    except Exception:
        print("An error occurred: {}".format(traceback.format_exc()))
