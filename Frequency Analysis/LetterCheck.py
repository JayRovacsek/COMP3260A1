import os

alphabet = list(map(chr, range(97, 123)))
cipher_text = ''
os.chdir('../')
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
    ext = os.path.splitext(file)[1]
    if ".bin" in ext:
        with open(file, mode='r') as text:
            for line in text:
                cipher_text += line
            for letter in alphabet:
                if letter not in cipher_text:
                    print("Letter: {} doesn't exist in cipher text from {}".format(letter,file))
            cipher_text = ''