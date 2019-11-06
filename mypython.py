import string
import random
import sys
random.seed()
fileLetters = ['A', 'B', 'C']
myfile = 'myfile'
for i in range(3):
    myfile = 'myfile' + fileLetters[i]
    file= open(myfile, "w+")
    randomString = ''
    for j in range(10):
        randomString += random.choice(string.ascii_lowercase)
    randomString += '\n'
    file.write(randomString)
    sys.stdout.write(randomString)
    file.close()
randomIntA = random.randint(1, 42)
print(randomIntA)
randomIntB = random.randint(1, 42)
print(randomIntB)
print(randomIntA * randomIntB)
