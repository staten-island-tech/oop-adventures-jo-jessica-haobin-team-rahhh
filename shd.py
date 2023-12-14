def fuhdas():
    user_input = int(input("insert number: "))
    divsor = 1
    prime = []
    while divsor <= user_input:
        if user_input%divsor == 0:
            prime.append(divsor)
        divsor += 1
    print(prime)


def ashdhas():
    x = input("racecar")
    if x == x[::-1]:
        print("palidrome")
    

ashdhas()