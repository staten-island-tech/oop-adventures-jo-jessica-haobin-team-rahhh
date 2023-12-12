def panagram(x):
    if len(x) < 26:
        return False
    n = set()
    for i in x:
        if not i in n:
            n.add(i)
            if len(n) == 26:
                return True
            return False
        #set means 133 is the same as 313