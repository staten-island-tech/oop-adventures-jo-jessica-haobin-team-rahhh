import os, time
def findcapitalletter(string):
    lister = []
    for letter in string:
        strlist = list(string)
        for letter in strlist:
            strlist.remove(letter)
            if letter.upper() == letter:
                lister.append(string.index(letter))
    return lister
print(findcapitalletter("TEsT"))