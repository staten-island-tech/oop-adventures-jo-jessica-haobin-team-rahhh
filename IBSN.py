x = input("enter number")
#10 or 13
def isISBN(x):
    if len(x) == 10 or len(x) == 13:
        return True
    else:
        return False