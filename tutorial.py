import json, os, random, time
from fighting import partsinbattle
data = open("./data.json", encoding="utf8")
data = json.load(data)
EXP = 0
os.system('cls')
class tut:
    global enemy_name
    enemy_name = data[4]['Name']
    def createcharacter():
        name = str(input("Please insert your name: "))
        print(f"There are 2 classes you can choose from. Warrior or Mage. What class will you choose {name}?")
        Options = ['Warrior', 'Mage']
        if Options != '':
            x = input(f"{'|'.join(Options)}: ").capitalize()
            while x not in Options:
                x = input(f"{'|'.join(Options)}: ").capitalize()
            return x
    

    def tutorial_part1():
        os.system('cls')
        input("To continue to the instructions to this game, click enter.")
        input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
        input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
        input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
        input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
        os.system('cls')
        input("Instructions: To attack, input E. To engage in the fight, input P.")
        input("You also roll 2 dice to determine if you attack or the enemy attacks.")
        input("Everytime you leave a battle, 10 EXP points will be deducted from you.")
        input("EXP points are used to level up, each level needs 100 EXP points. Once you get to a high enough level, you may fight with the final boss...")

    def tutorial_part2():
        global EXP
        input("In this game both you and the enemy will have 100 HP. To continue to the instructions to this game, click enter.")
        os.system('cls')
        input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
        input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
        input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
        input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
        j = tut.createcharacter()
        if j == "Warrior":
            print(f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}.")
            while EXP <= 100:
                e = random.randint(0,3)
                f = data[e]['Name']
                d = (input(f"You've encounter an {f}, press P to engage: ")).upper()
                while d != "P":
                    d = (input(f"You've encounter an {f}, press P to engage: ")).upper()
                os.system('cls')
                if d == "P":
                    os.system('cls')
                    g = partsinbattle.warrior_fight(f)
                    if g == True:
                        EXP += data[e]['Exp']
                        print(f"You've currently have {EXP} exp.")
                        input("Press any buttons to continue: ")
                    elif g == False:
                        EXP -= data[e]['Exp']
                        print(f"You've currently have {EXP} exp.")
                        input("Press any buttons to continue: ")
                         
                while EXP <= 100:
                    os.system('cls')
                    encounterenemy = (input("You've encounter an enemy, press P to engage or press R to run: ")).upper()
                    while encounterenemy != "P" and encounterenemy != "R":
                        encounterenemy = (input("You've encounter an enemy, press P to engage or press R to run: ")).upper()
                    if encounterenemy == "P":
                                os.system('cls')
                                a = random.randint(0,3)
                                b = data[a]['Name']
                                c = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                                while c != "E" and "R":
                                    c = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                                os.system('cls')
                                if c == "E":
                                    os.system('cls')
                                    h = partsinbattle.warrior_fight(b)
                                    if h == True:
                                        EXP += data[a]['Exp']
                                        print(f"You've currently have {EXP} exp.")
                                        input("Press any buttons to continue: ")
                                    elif h == False: 
                                        EXP -= data[a]['Exp']
                                        print(f"You've currently have {EXP} exp.")
                                        input("Press any buttons to continue: ")
                                elif c == "R": 
                                    EXP -= 10 
                                    os.system('cls')
                                    print("You've ran away...")
                                    print('Game Over')
                                    break
                    elif encounterenemy == "R":
                        EXP -= 10
                        os.system('cls')
                        print("You've ran away...")
                        print('Game Over')
                        return
                    
        if j == "Mage": 
            print(f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}.")
            while EXP <= 100:
                e = random.randint(0,3)
                f = data[e]['Name']
                d = (input(f"You've encounter an {f}, press P to engage: ")).upper()
                while d != "P":
                    d = (input(f"You've encounter an {f}, press P to engage: ")).upper()
                os.system('cls')
                if d == "P":
                    os.system('cls')
                    g = partsinbattle.mage_fight(f)
                    if g == True:
                        EXP += data[e]['Exp']
                        print(f"You've currently have {EXP} exp.")
                        input("Press any buttons to continue: ")
                    elif g == False:
                        EXP -= data[e]['Exp']
                        print(f"You've currently have {EXP} exp.")
                        input("Press any buttons to continue: ")
                
                while EXP <= 100:
                    encounterenemy = (input("You've encounter an enemy, press P to engage or press R to run: ")).upper()
                    while encounterenemy != "P" and encounterenemy != "R":
                        encounterenemy = (input("You've encounter an enemy, press P to engage or press R to run: ")).upper()
                    os.system('cls')
                    if encounterenemy == "P":
                                a = random.randint(0,3)
                                b = data[a]['Name']
                                c = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                                while c != "E" and c != "R":
                                    c = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                                os.system('cls')
                                if c == "E":
                                    os.system('cls')
                                    h = partsinbattle.mage_fight(b)
                                    if h == True:
                                        EXP += data[a]['Exp']
                                        print(f"You've currently have {EXP} exp.")
                                        input("Press any buttons to continue: ")
                                    elif h == False: 
                                        EXP -= data[a]['Exp']
                                        print(f"You've currently have {EXP} exp.")
                                        input("Press any buttons to continue: ")
                                elif c == "R": 
                                    EXP -= 10 
                                    os.system('cls')
                                    print("You've ran away...")
                                    print('Game Over')
                                    break
                                else: 
                                    input(c)
                    elif encounterenemy == "R":
                        EXP -= 10
                        os.system('cls')
                        print("You've ran away...")
                        print('Game Over')
                        return

        if EXP >= 100:
            return EXP
        
    






