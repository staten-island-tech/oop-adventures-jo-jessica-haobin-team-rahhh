from realclasses import warrior, mage
from fighting import player, warrior_fight, mage_fight, h
import os, random, json
data = open("./data.json", encoding="utf8")
data = json.load(data)
os.system('cls')

class finalboss:
    def makeboss():
        enemy_name =
    def thefight():
        os.system('cls')
        print('This is the final battle!!! Beware and be prepare!!!')
        input("If you're still willing to continue press any buttons to go on: ")
        os.system('cls')
        player.createplayer()
        if h == "Warrior":
            warrior_fight()
        elif h == "Mage":
            mage_fight()

finalboss.thefight()