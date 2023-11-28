from merchant import Merchant


NPC = Merchant("MERCHANT", ["Gun", "Sword", "Healing-Potion", "Toy-Goblin"])

Buy = input("What item would you like to buy?")
item = NPC.sell()




""" def tutorial():
    enemy_name = "Mr.Whalen"
    sukds = input("In this game both you and the enemy will have 100 HP. To continue to the instructions to this game, click enter.")
    dsoa = input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
    adi = input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
    usu = input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
    hsdo = input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
    dsoh = input("Instructions: To attack, input E. To heal, input H. To engage in the fight, input P. To run away, input R. To equip your weapon or unequip your weapon, input E. ")
    name = input("Please insert your name: ").title()
    x = input(f"Theres two types of classes in this game: Mage and Warrior. What class will you choose {name}? ").title()

    if x == "Warrior":
        sesf = f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}."
        EXP = 0
        while EXP != 100:
            encounterenemy = input("You've encounter an enemy, press P to engage or press R to run: ").title()
            if encounterenemy == "P":
                    import random
                    a = random.randint(0,3)
                    enemies = ["dragon", "goblin", "zombie", "skeleton"]
                    b = enemies[a]
                    adshiu = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                    if adshiu == "E":
                         from wts import fight
                    elif adshiu == "R": 
                         sd = input("You've ran away... The game is over.")
                         break
                    else: 
                         print("ERROR")



                




tutorial()

def fighting():
    input("Now that you picked a class, you are allowed to ") """