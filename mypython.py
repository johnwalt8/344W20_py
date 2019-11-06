import string
import random
fileLetters = ['A', 'B', 'C']
myfile = 'myfile'
for i in range(3):
    myfile = 'myfile' + fileLetters[i]
    file= open(myfile, "w+")
    randomString = ''
    for i in range(10):
        randomString += random.choice(string.ascii_lowercase)
    randomString += '\n'
    file.write(randomString)
    file.close()

