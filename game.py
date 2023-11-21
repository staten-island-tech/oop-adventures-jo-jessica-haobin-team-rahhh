from classes2 import warrior
from classes2 import mage
from classes2 import enemy



def tutorial():
    sukds = input("In this game both you and the enemy will have 100 HP. To continue to the instructions to this game, click enter.")
    dsoh = input("To attack, input Y. To heal, input H. To engage in the fight, input P. To run away, input S. To equip your weapon or unequip your weapon, input E. ")
    name = input("Please insert your name: ").title()
    x = input(f"Theres two types of classes in this game: Mage and Warrior. What class will you choose {name}? ").title()

    if x == "Warrior":
        c = input("Now that you chosen a character.. Would you like to fight the enemy now?: ").title
        if c == "No":
            
            print()
        while c == "Yes":
            attack = input("The enemy has appeared, it has 100 health, would you like to attack it? Y/N: ").title()
            if attack == "Y":
                enemy(100,20)
                




tutorial()

def fighting():
    input("Now that you picked a class, you are allowed to ")