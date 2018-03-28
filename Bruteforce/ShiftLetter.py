#!/usr/bin/python
import os

USELESS_CHARS = [' ']

def ShiftCipher(cipherText,file):
    os.chdir('Bruteforce/Results')
    filename = os.path.splitext(file)[0]+"_Results"
    count = 0
    newText = ""
    while count < 26:
        with open(filename, 'a') as f:
            if count == 0:
                f.write("Original: {}\n".format(cipherText))
                count += 1
            else:
                for char in cipherText:
                    newText += ShiftText(char,count)
                f.write("Result {}: {}\n".format(count,newText))
                count += 1
            newText=""
    os.chdir('../..')

def ShiftText(char,shift):
    x=ord(char)
    y=x+shift
    if y > 122:
        y -= 26
    return chr(y)
        

def GetCipherText(file):
    cipherText = ""
    with open(file, 'r') as f:
        line = [list(line.rstrip()) for line in f]
        for chars in line:
            for char in chars:
                if char not in USELESS_CHARS:
                    cipherText += char
    ShiftCipher(cipherText,file)

def DetermineFiles():
    os.chdir('..')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in  files:
        extension = os.path.splitext(file)[1].lower()
        if extension == '.bin':
            print('Matched binary file called: {}\n'.format(file))
            GetCipherText(file)

def CheckResults():
    os.chdir('Bruteforce/Results')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        count = 0
        with open(file, 'r') as result:
            for line in result:
                if "the" in line:
                    print("Potential Plaintext in {}, using shift {}".format(file,count))
                count += 1

if __name__ == "__main__":
    DetermineFiles()
    CheckResults()