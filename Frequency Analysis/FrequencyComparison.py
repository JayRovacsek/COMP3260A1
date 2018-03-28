import os

USELESS_CHARS = [' ']

def CalculateFrequencies(file):
    charcount = []
    seenchars=[]
    totalCount = 0
    with open(file, 'r') as f:
        line = [list(line.rstrip()) for line in f]
    for chars in line:
        for char in chars:
            if char not in charcount and char not in USELESS_CHARS and char not in seenchars:
                charcount.append([char,1])
                seenchars.append(char)
                totalCount += 1
            elif char not in USELESS_CHARS:
                for charrecord in charcount:
                    if char in charrecord[0]:
                        index = seenchars.index(char)
                        count = charcount[index][1]
                        charcount[index][1] = count + 1
                        totalCount += 1
    charcount.sort(key=lambda charcount: charcount[1],reverse=True)
    print('Processed {} total chars\nChar frequencies: {}\nTotal unique chars: {}\n'.format(totalCount,charcount,len(charcount)))
    print('============================================================================================\n')

def DetermineFiles():
    os.chdir('..')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in  files:
        extension = os.path.splitext(file)[1].lower()
        if extension == '.bin':
            print('Matched binary file called: {}\n'.format(file))
            CalculateFrequencies(file)

if __name__ == "__main__":
    DetermineFiles()