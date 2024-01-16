import json, os, time, random
from fighting import fight, partsinbattle
data = open("./data.json", encoding="utf8")
data = json.load(data)
EXP = 0
os.system('cls')
class tut:
    global enemy_name
    enemy_name = data[4]['Name']
    def createcharacter():
        name = str(input("Please insert your name: "))
        x = (input(f"Theres two types of classes in this game: Mage and Warrior. What class will you choose {name}?: ")).lower()
        return x
    
    def tutorial_part1():
        os.system('cls')
        input("To continue to the instructions to this game, click enter.")
        input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
        input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
        input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
        input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
        input("You were given 200 coins to start with and 100 HP.")
        input("Instructions: To attack, input E. To engage in the fight, input P.")
        input("You also roll 2 dice to determine if you attack or the enemy attacks.")
        input("Everytime you leave a battle, 10 EXP points will be deducted from you.")
        input("EXP points are used to level up, each level needs 100 EXP points. Once you get to a high enough level, you may fight with the final boss...")

    def tutorial_part2():
        global EXP
        os.system('cls')
        input("In this game both you and the enemy will have 100 HP. To continue to the instructions to this game, click enter.")
        input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
        input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
        input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
        input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
        
        j = tut.createcharacter()

        if j == "warrior":
            print(f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}.")
            while EXP <= 100:
                e = random.randint(0,3)
                f = data[e]['Name']
                d = (input(f"You've encounter an {f}, press P to engage: ")).upper()
                os.system('cls')
                if d == "P":
                    g = partsinbattle.warrior_fight(f)
                    if g == True:
                        EXP += data[e]['Exp']
                        print(f"You've currently have {EXP} exp.")
                    elif g == False:
                        EXP -= data[e]['Exp']
                         
                while EXP <= 100:
                    encounterenemy = (input("You've encounter an enemy, press P to engage or press R to run: ")).upper()
                    if encounterenemy == "P":
                                a = random.randint(0,3)
                                b = data[a]['Name']
                                c = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                                if c == "E":
                                    h = partsinbattle.warrior_fight(b)
                                    if h == True:
                                        EXP += data[a]['Exp']
                                        print(f"You've currently have {EXP} exp.")
                                    elif h == False: 
                                        EXP -= data[a]['Exp']
                                        print(f"You've currently have {EXP} exp.")
                                elif c == "R": 
                                    EXP -= 10 
                                    print("You've ran away...")
                                    print('Game Over')
                                    break
                                else: 
                                    print("ERROR")
        if j == "mage": 
            print(f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}.")
            while EXP <= 100:
                e = random.randint(0,3)
                f = data[e]['Name']
                d = (input(f"You've encounter an {f}, press P to engage: ")).upper()
                os.system('cls')
                if d == "P":
                    g = partsinbattle.mage_fight(f)
                    if g == True:
                        EXP += data[e]['Exp']
                        print(f"You've currently have {EXP} exp.")
                    elif g == False:
                        EXP -= data[e]['Exp']
                         
                while EXP <= 100:
                    encounterenemy = (input("You've encounter an enemy, press P to engage or press R to run: ")).upper()
                    if encounterenemy == "P":
                                a = random.randint(0,3)
                                b = data[a]['Name']
                                c = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                                if c == "E":
                                    h = partsinbattle.mage_fight(b)
                                    if h == True:
                                        EXP += data[a]['Exp']
                                        print(f"You've currently have {EXP} exp.")
                                    elif h == False: 
                                        EXP -= data[a]['Exp']
                                        print(f"You've currently have {EXP} exp.")
                                elif c == "R": 
                                    EXP -= 10 
                                    print("You've ran away...")
                                    print('Game Over')
                                    break
                                else: 
                                    print("ERROR")
        if EXP >= 100:
            return EXP
        
    








