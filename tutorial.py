from realclasses import warrior
from realclasses import mage
from realclasses import enemy



def tutorial():
    EXP = 0
    enemy_name = "Mr.Whalen"
    print("In this game both you and the enemy will have 100 HP. To continue to the instructions to this game, click enter.")
    print("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
    print(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
    print(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
    print(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
    print("Instructions: To attack, print Y. To heal, print H. To engage in the fight, print P. To run away, print S. To equip your weapon or unequip your weapon, print E. ")
    name = input("Please insert your name: ").title()
    x = print(f"Theres two types of classes in this game: Mage and Warrior. What class will you choose {name}? ").title()

    if x == "Warrior":
        print(f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}.")
        while EXP != 100:
            eihd = input("You've encounter an enemy, press P to engage: ").title()
            if eihd == "P":
                def engage_fight():
                    

        c == input("Now that you're high enough level.. Would you like to fight the enemy now?: ").title
        if c == "No":
            
        while c == "Yes":
            attack = input("The enemy has appeared, it has 100 health, would you like to attack it? Y/N: ").title()
            if attack == "Y":
                enemy(100,20)
                




tutorial()

def fighting():
    print("Now that you picked a class, you are allowed to ")