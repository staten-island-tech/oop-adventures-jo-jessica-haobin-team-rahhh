import os, time
def findcapitalletter(string):
    lister = []
    for letter in string:
        strlist = list(string)
        for letter in strlist:
            if letter.upper() == letter:
                lister.append(string.index(letter))

    return lister


ste = ['S', 'S', 'S', 'A', 'D']
print(ste.remove('S'))