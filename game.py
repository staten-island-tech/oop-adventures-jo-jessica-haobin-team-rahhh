from classes2 import warrior
from classes2 import mage
from classes2 import enemy



def tutorial():
    enemy_name = "Mr.Whalen"
    sukds = input("In this game both you and the enemy will have 100 HP. To continue to the instructions to this game, click enter.")
    dsoa = input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
    adi = input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
    usu = input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
    hsdo = input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
    dsoh = input("Instructions: To attack, input Y. To heal, input H. To engage in the fight, input P. To run away, input S. To equip your weapon or unequip your weapon, input E. ")
    name = input("Please insert your name: ").title()
    x = input(f"Theres two types of classes in this game: Mage and Warrior. What class will you choose {name}? ").title()

    if x == "Warrior":
        sesf = f"Now that you chosen your class, you need to collect EXP in order to be a high enough level to fight {enemy_name}."
        EXP = 0
        while EXP != 100:
            eihd = input("You've encounter an enemy, press P to engage: ").title()
            if eihd == "P":
                def engage_fight():
                    

        c = input("Now that you're high enough level.. Would you like to fight the enemy now?: ").title
        if c == "No":
            
            print()
        while c == "Yes":
            attack = input("The enemy has appeared, it has 100 health, would you like to attack it? Y/N: ").title()
            if attack == "Y":
                enemy(100,20)
                




tutorial()

def fighting():
    input("Now that you picked a class, you are allowed to ")