def factor(x):
    global y
    for i in range(1, x+1):
        if x%i == 0:
            y = print(i)

factor(10)

def prime_or_not(x):
    global y
    factor(x)
    if y[0] == 1:
        if y[1] == x:
            print('prime')
    else:
        print('not prime')

prime_or_not(10)