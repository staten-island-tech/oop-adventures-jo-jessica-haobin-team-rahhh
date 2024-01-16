class tut:
    def __init__(self, enemys_name):
        self.enemys_name = enemys_name
    def tutorial(self):
        sukds = input("To continue to the instructions to this game, click enter.")
        dsoa = input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
        adi = input(f"Until one day they were attacked by a enemy who goes by {self.enemys_name}. He was feared throughout the years and until now he didn't attack.")
        usu = input(f"The kingdom was broken down and {self.enemys_name} took over the area. Houses were burned and people were turned into slaves.")
        hsdo = input(f"It is up to you, to defeat {self.enemys_name} and restore the kingdom.")
        items_given_by_me = input("You were given 200 coins to start with and 100 HP.")
        dsoh = input("Instructions: To attack, input E. To heal, input H. To engage in the fight, input P. To leave away, input L. To equip your weapon or unequip your weapon, input E. ")
        adsihd = input("Everytime you leave a battle, 10 EXP points will be deducted from you.")
        dsagudsiuhddhaisihadsiuhadsiuhadsiuhads = input("EXP points are used to level up, each level needs 100 EXP points. Once you get to a high enough level, you may fight with the final boss...")


def tutorial():
    enemy_name = "Mr.Whalen"
    print("In this game both you and the enemy will have 100 HP. To continue to the instructions to this game, click enter.")
    print("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
    print(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
    print(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
    print(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
    print("Instructions: To attack, print E. To heal, print H. To engage in the fight, print P. To run away, print R. To equip your weapon or unequip your weapon, print E. ")
    name = str(input("Please insert your name: "))
    x = (print(f"Theres two types of classes in this game: Mage and Warrior. What class will you choose {name}? ")).lower()

    if x.capitalize() == "Warrior":
        print(f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}.")
        EXP = 0
        while EXP != 100:
            a = input("You've encounter an enemy, press P to engage: ")
            if a == "P":
                from fighting import fight
                fight()


        encounterenemy = (input("You've encounter an enemy, press P to engage or press R to run: ")).upper()
        if encounterenemy == "P":
                    import random
                    a = random.randint(0,3)
                    enemies = ["dragon", "goblin", "zombie", "skeleton"]
                    b = enemies[a]
                    c = input(f"You've encountered an {b}! Enter E to attack, R to run away: ").upper()
                    if c == "E":
                         from fighting import fight
                         from fighting import enemy
                         dragon = enemy('Dragon', '200', 'Hybrid', 50)
                         fight(dragon, )
                    elif c == "R": 
                         sd = print("You've ran away... The game is over.")
                       
                    else: 
                         print("ERROR")



        a = input("You've encounter an enemy, press P to engage: ").title()
        if a == "P":
                from fighting import fight
                fight()
                    
            




tutorial()

def fighting():
    print("Now that you picked a class, you are allowed to ")

