# Author: Cody Lewis
# Date: 04-APR-2018
# Based on information from https://inventwithpython.com/hacking/chapter9.html
import sys
import traceback
import math

def decrypt(key,message):
    cols = math.ceil(len(message)/key)
    rows = key
    nullBoxNum = (cols * rows) - len(message)

    plaintext = ['']*cols

    m = 0 # running column number
    n = 0 # running row number

    for symbol in message:
        plaintext[m]+=symbol
        m+=1
        if(m == cols) or (m == cols-1 and n >= rows - nullBoxNum):
            m = 0
            n+=1

    return ''.join(plaintext) # put together the disjoint strings

if __name__ == "__main__":
    try:
        if len(sys.argv) is 1:
            message = input("Enter your ciphertext: ")
            key = int(input("Enter the key: "))
            decryption = decrypt(key,message)
            print("The decrypted message is:\n{}".format(decryption))
        else:
            args = sys.argv
            del args[0]
            i = 0
            while(i < len(args)):
                key = int(args[i])
                if(i+1 < len(args)):
                    message = args[i+1]
                    print("The decrypted message is:\n{}".format(decrypt(key,message)))
                    i = i+2
                else:
                    print("Not enough arguments")
                    break
    except Exception:
        print(traceback.format_exc())
