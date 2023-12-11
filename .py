c = 0
def factor(x):
    global c
    for i in range(1, x+1):
        if x%i == 0:
            c += 1


def prime_or_not(x):
    global c
    factor(x)
    if c == 2:
        print('prime')
    else:
        print('not prime')


prime_or_not(11923)