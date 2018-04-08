#!/usr/bin/python
import os,traceback,sys

def translateToAlphaKey(key):
    alpha_key = ''
    chars = key.split(",")
    for char in chars:
        if char.isnumeric():
            new_char = 97+(int(char)%26)
            alpha_key += chr(new_char)
        else:
            if ord(char) < 95:
                new_char = 97 + (ord(char)%48)
                alpha_key += (chr(new_char%128))
            else:
                alpha_key += char
    return alpha_key

def translateToNumericKey(key):
    numeric_key = ''
    for char in key:
        if len(numeric_key):
            numeric_key += ','+str(ord(char)-97)
        else:
            numeric_key += str(ord(char)-97)
    return numeric_key

def decrypt(key,file):
    print("Starting decrypt using key: {}".format(key))
    if "," in key:
        print("Decrypt using alpha translated key: {}".format(translateToAlphaKey(key)))
        key_length = sum(1 for k in key.split(","))
    else:
        key_length = len(key)

    cipher_text = ''
    with open(file, mode='r') as text:
        for line in text:
            cipher_text += line
    cipher_text = cipher_text.replace('\n','').replace(' ','')
    column_or_row_count = int(len(cipher_text) / key_length)
    decryptColumn(column_or_row_count,cipher_text)
    print("------------------------------")
    #decryptRow(column_or_row_count,cipher_text)

def decryptColumn(column_length,cipher_text):
    i = 0
    plain_text = []
    for char in cipher_text:
        if len(plain_text) is not column_length:
            plain_text.append([char])    
        else:
            plain_text[i].append(char)
        i += 1
        if i+1 is column_length:
            i=0
    for l in plain_text:
        print(l)

def decryptRow(row_length,cipher_text):
    ## This is a filthy mess, and I will fix this shortly
    i = 0
    r = 0
    plain_text = [[]]
    for char in cipher_text:
        if r is not 0:
            print(plain_text)
            print(len(plain_text))
            if len(plain_text[i]) is not row_length:
                plain_text[r].append(char)    
            else:
                plain_text[r].append([char])
                r += 1
            i += 1
            if i+1 is row_length:
                i=0
        else:
            if len(plain_text) is not row_length:
                plain_text[0].append(char)    
            else:
                plain_text.append([char])
                r += 1
            i += 1
            if i+1 is row_length:
                i=0
    for l in plain_text:
        print(l)

if __name__ == "__main__":
    if len(sys.argv) is 1:
        key = input("Enter the key you want to check: ")
        decrypt(key,'../c4.bin')
    else:
        args = sys.argv
        del args[0]
        if len(args) is 1:
            decrypt(args[0],'../c4.bin')
        else:
            decrypt(args[:-1],'../c4.bin')