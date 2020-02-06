# mypython.py
# Walter Johnson
# Program Py: CS344 Operating Systems I, Winter 2020

import string
import random
import sys

# takes a quantity, a string for the file name, and more strings that will each be appended to the file name; returns a list of the names of the files created
def createFilesContainingRandomString(stringLength, fileName, *fileNameSuffixes):
    fileNameList = []
    for fileNameSuffix in fileNameSuffixes: # for each of the strings to be appended
        myfile = fileName + fileNameSuffix
        myString = createRandomString(stringLength)
        file = open(myfile, "w+")
        file.write(myString)
        file.close()
        fileNameList.append(myfile)
    return fileNameList

# takes a number for the length of the string to be created, returns the string
def createRandomString(numElements):
    randomString = ''
    for i in range(numElements): 
        randomString += random.choice(string.ascii_lowercase)
    randomString += '\n'
    return randomString

# takes a list of files names, writes entire contents of each file to standard output
def readAndPrintFileContents(fileNameList):
    for fileName in fileNameList:
        file = open(fileName, "r")
        fileContents = file.read()
        sys.stdout.write(fileContents)
        file.close()

# takes a pair of integers representing minimum and maximum value, returns integer
def createAndPrintRandomInt(min, max):
    randomInt = random.randint(min, max)
    print(randomInt)
    return randomInt

def main():
    random.seed()

    listOfFileNames = createFilesContainingRandomString(10, 'myfile', 'A', 'B', 'C')

    readAndPrintFileContents(listOfFileNames)

    # after random ints are printed, multiplies those ints and prints product
    print(createAndPrintRandomInt(1, 42) * createAndPrintRandomInt(1, 42))

main()