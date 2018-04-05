#!/usr/bin/python
import os
import traceback

USELESS_CHARS = [' ']

def calculate_frequency(file):
    print("File processed: {}".format(file))
    charCount = {}
    charFreq = {}
    totalCount = 0
    with open(file, 'r') as f:
        line = [list(line.rstrip()) for line in f]
    for chars in line:
        for char in chars:
            try:
                if char not in charCount and char not in USELESS_CHARS:
                    charCount[char]=1
                    totalCount += 1
                elif char not in USELESS_CHARS:
                    if char in charCount:
                        count = charCount[char]+1
                        charCount.pop(char)
                        charCount[char]=count
                        totalCount += 1
            except Exception:
                print("Error occured: {} on char: {}".format(traceback.format_exc(),char))
    for charEntry in charCount:
        frequency = charCount[charEntry]/totalCount
        charFreq[charEntry]=round(frequency*100,5)
    print('Processed {} total chars\nChar frequencies: {}\nTotal unique chars: {}\n'.format(totalCount,[(k,v) for k,v in charCount.items()],len(charCount)))
    sortedCharFreq = [(k,v) for k,v in charFreq.items()]
    for key, value in sortedCharFreq:
        print("Letter: {} Frequency: {}%".format(key,value))
    print('============================================================================================\n')

def determine_files():
    os.chdir('..')
    matched = {}
    count=0
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in  files:
        extension = os.path.splitext(file)[1].lower()
        if extension == '.bin':
            print('Matched binary file called: {}\n'.format(file))
            matched[file]=count
            count+=1
    return matched

if __name__ == "__main__":
    files = determine_files()
    for file in files:
        calculate_frequency(file)