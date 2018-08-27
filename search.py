import os
import re
Prefix = r'(abc)*'

def readFile(pathName):  # defining function that reads the file line by line

    with open(pathName, 'r') as text:  # importing text to be checked, provided in txt file

        for line in text:
            yield line


for root, dirs, files in os.walk('C:\Users\dprzystu\Desktop\porownanie'):
    for file in files:
        if file.endswith('.xlsx'):
            pathToFile = os.path.join(root, file)

            allLines = readFile(pathToFile)  # reading the file
            for lineData in allLines:

                matching = re.search(Prefix, lineData)  # finding all lines matching the pattern. Flag means that ^ and $ are valid for each line not whole document.
                if matching is not None:  # checking if pattern is found

                        print file
                        break
