#!/usr/bin/python
import os

USELESS_CHARS = [' ']

def shift_cipher(cipherText,file):
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
                    newText += shift_text(char,count)
                f.write("Result {}: {}\n".format(count,newText))
                count += 1
            newText=""
    os.chdir('../..')

def shift_text(char,shift):
    x=ord(char)
    y=x+shift
    if y > 122:
        y -= 26
    return chr(y)
        

def get_cipher_text(file):
    cipherText = ""
    with open(file, 'r') as f:
        line = [list(line.rstrip()) for line in f]
        for chars in line:
            for char in chars:
                if char not in USELESS_CHARS:
                    cipherText += char
    shift_cipher(cipherText,file)

def determine_files():
    os.chdir('..')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in  files:
        extension = os.path.splitext(file)[1].lower()
        if extension == '.bin':
            print('Matched binary file called: {}\n'.format(file))
            get_cipher_text(file)

def check_results():
    os.chdir('Bruteforce/Results')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        count = 0
        with open(file, 'r') as result:
            for line in result:
                if "that" in line:
                    print("Potential Plaintext in {}, using shift {}".format(file,count))
                count += 1

if __name__ == "__main__":
    determine_files()
    check_results()