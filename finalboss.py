from realclasses import warrior, mage
from fighting import warrior_fight, mage_fight, dialogue, fight
import os, random, json
data = open("./data.json", encoding="utf8")
data = json.load(data)
os.system('cls')

class finalboss:
    def thefight():
        enemy_name = 'Mr.Whalen'
        h = dialogue(['Choose between Warrior and Mage: '], ['Warrior', 'Mage'])
        os.system('cls')
        print('This is the final battle!!! The monster Mr.Whalen is scary and dangerous!!! His head lights up the room with ominous white light!!! Beware and be prepare!!!')
        input("If you're still willing to continue press any buttons to go on: ")
        os.system('cls')
        if h == "Warrior":
            warrior_fight(enemy_name)
        elif h == "Mage":
            mage_fight(enemy_name)


def capital_indexes(string):
    for letter in string:
        if letter.capitalize() == string:
            print(letter.capitalize())
        
capital_indexes("HeLlO")
