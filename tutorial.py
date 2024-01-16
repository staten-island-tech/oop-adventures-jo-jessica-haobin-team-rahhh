import json, os
data = open("./data.json", encoding="utf8")
data = json.load(data)
EXP = 0
class tut:
    global enemy_name
    enemy_name = data[4]['Name']
    def tutorial_part1():
        input("To continue to the instructions to this game, click enter.")
        input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
        input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
        input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
        input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
        input("You were given 200 coins to start with and 100 HP.")
        input("Instructions: To attack, input E. To heal, input H. To engage in the fight, input P. To leave away, input L. To equip your weapon or unequip your weapon, input E. ")
        input("Everytime you leave a battle, 10 EXP points will be deducted from you.")
        input("EXP points are used to level up, each level needs 100 EXP points. Once you get to a high enough level, you may fight with the final boss...")

    def tutorial_part2():
        input("In this game both you and the enemy will have 100 HP. To continue to the instructions to this game, click enter.")
        input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
        input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
        input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
        input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
        input("Instructions: To attack, print E. To heal, print H. To engage in the fight, print P. To run away, print R. To equip your weapon or unequip your weapon, print E. ")
        name = str(input("Please insert your name: "))
        x = (input(f"Theres two types of classes in this game: Mage and Warrior. What class will you choose {name}?: ")).lower()

        if x.capitalize() == "Warrior":
            print(f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}.")
            while EXP != 100:
                a = (input("You've encounter an enemy, press P to engage: ")).capitalize()
                if a == "P":
                    import random
                    from fighting import fight
                    fight()
                    if fight() != True: 
                        return
                    else: 
                        return


            encounterenemy = (input("You've encounter an enemy, press P to engage or press R to run: ")).upper()
            if encounterenemy == "P":
                        import random
                        a = random.randint(0,3)
                        b = data[a]['Name']
                        c = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                        if c == "E":
                            from fighting import fight
                            fight()
                        elif c == "R": 
                            print("You've ran away...")
                            print('Game Over')
                        
                        else: 
                            print("ERROR")


                        
                

while EXP != 100:
    a = (input("You've encounter an enemy, press P to engage: ")).capitalize()
    if a == "P":
        from fighting import fight
        if fight() == True: 
            break
        elif fight() != True:
            break




