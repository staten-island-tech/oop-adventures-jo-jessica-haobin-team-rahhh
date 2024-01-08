import os, time
def findcapitalletter(string):
    list = []
    for letter in string:
        if letter.upper() == letter:
            list.append(letter)
    return list
print(findcapitalletter('HeLlO'))


os.system('cls')
i = 2
while True:
    time.sleep(1)
    i**=2
    print(i)