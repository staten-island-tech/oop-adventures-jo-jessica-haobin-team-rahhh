from fighting import partsinbattle, dialogue
import os, json
data = open("./data.json", encoding="utf8")
data = json.load(data)
os.system('cls')


def thebossbattle():
    enemy_name = 'Mr.Whalen'
    h = dialogue(['Choose between Warrior and Mage: '], ['Warrior', 'Mage'])
    os.system('cls')
    print('This is the final battle!!! The monster Mr.Whalen is scary and dangerous!!! His head lights up the room with ominous white light!!! Beware and be prepare!!!')
    input("If you're still willing to continue press any buttons to go on: ")
    os.system('cls')
    if h == "Warrior":
        partsinbattle.warrior_fight(enemy_name)
    elif h == "Mage":
        partsinbattle.mage_fight(enemy_name)
thebossbattle()