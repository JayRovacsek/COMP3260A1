#!/usr/bin/python
import os

USELESS_CHARS = [' ']

def CalculateFrequencies(files):
    for file in files:
        print("File processed: {}".format(file))
        charCount = []
        charFreq = []
        seenChars=[]
        totalCount = 0
        with open(file, 'r') as f:
            line = [list(line.rstrip()) for line in f]
        for chars in line:
            for char in chars:
                try:
                    if char not in charCount and char not in USELESS_CHARS and char not in seenChars:
                        charCount.append([char,1])
                        seenChars.append(char)
                        totalCount += 1
                    elif char not in USELESS_CHARS:
                        for charrecord in charCount:
                            if char in charrecord[0]:
                                index = seenChars.index(char)
                                count = charCount[index][1]
                                charCount[index][1] = count + 1
                                totalCount += 1
                except Exception:
                    print("Error occured: {} on char: {}".format(Exception,char))
        for charEntry in charCount:
            frequency = charEntry[1]/totalCount
            charFreq.append([charEntry[0],round(frequency*100,5)])
        charFreq.sort(key=lambda charFreq: charFreq[1],reverse=True)
        charCount.sort(key=lambda charCount: charCount[1],reverse=True)
        print('Processed {} total chars\nChar frequencies: {}\nTotal unique chars: {}\n'.format(totalCount,charCount,len(charCount)))
        for entry in charFreq:
            print("Letter: {} Frequency: {}%".format(entry[0],entry[1]))
        print('============================================================================================\n')

def DetermineFiles():
    os.chdir('..')
    matched = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in  files:
        extension = os.path.splitext(file)[1].lower()
        if extension == '.bin':
            print('Matched binary file called: {}\n'.format(file))
            matched.append(file)
    return matched

if __name__ == "__main__":
    files = DetermineFiles()
    CalculateFrequencies(files)