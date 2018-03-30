#!/usr/bin/python
# Credit for this goes to: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
from functools import reduce
import sys

def factors(n):    
    return(sorted(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))))

if __name__ == "__main__":
    try:
        if len(sys.argv) is 1:
            i = input("Enter a number:")
            factors(int(i))
        else:
            args = sys.argv
            del args[0]
            for arg in args:
                factorList = factors(int(arg))
                print("Factors of {} are: {}".format(arg,factorList))
    except Exception:
        print(Exception)
