import sys
def FastExp(base,expon,modulus):
    if modulus is 1:
        return 0
    else:
        res = 1
        base = base%modulus
        while(expon > 0):
            if(expon%2 == 1):
                res = (res*base) % modulus
                expon-=1
            else:
                base = (base*base) % modulus
                expon/=2
        return res
if __name__ == "__main__":
    if len(sys.argv) is 1:
        base = int(input("Input your base number: "))
        expon = int(input("Input your exponent: "))
        modulus = int(input("Input your modulus: "))
        print("Your answer is {}".format(FastExp(base,expon,modulus)))
    else:
        args = sys.argv
        del args[0]
        i = 0
        while(i < len(args)):
            base = int(args[i])
            expon = int(args[i+1])
            modulus = int(args[i+2])
            print("Your answer is {}".format(FastExp(base,expon,modulus)))
            i+=3
