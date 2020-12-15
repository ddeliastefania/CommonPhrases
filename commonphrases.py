import sys
import magic
import re


def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    file_content1 = readfile(file1)
    file_content2 = readfile(file2)

    if file_content1 != 'Error!' and file_content2 != 'Error!':
        firstsplit = splitphrases(file_content1)
        firstlist = makelistofwords(firstsplit)

        secondsplit = splitphrases(file_content2)
        secondlist = makelistofwords(secondsplit)

        print('Common phrases: ')
        print(comparephrases(firstlist, secondlist))
    else:
        print('Wrong content file')


def readfile(filename):
    f = magic.Magic(mime=True)
    istext = f.from_file(filename)
    if istext == 'text/plain':
        file = open(filename, "r")
        list = file.read()
        file.close()
        return list
    else:
        return 'Error!'


def splitphrases(continut):
    split = re.split('[?!.]', continut)
    variabila = repairsentence(split)
    return variabila


def repairsentence(allcontent):
    newlist=[]
    for phrase in allcontent:
        newphrase = phrase.replace('\n', '')
        if newphrase:
            newlist.append(newphrase)
    return newlist


def splitinwords(phrase):
    validlist=[]
    wordslist = re.split('[,(); ]', phrase)
    for word in wordslist:
        if word:
            validlist.append(word)
    return validlist


def makelistofwords(listofphrases):
    listofwords = []
    for phrase in listofphrases:
        listofwords.append(splitinwords(phrase))
    return listofwords


def comparephrases(firstlist, secondlist):
    commonphrases=[]
    for list1 in firstlist:
        for list2 in secondlist:
            if list1 == list2:
                commonphrases.append(list1)
    return commonphrases

main()