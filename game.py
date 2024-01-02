from merchant import Merchant
from user import User
from enemy import ENEMY
import random, os
from tutorial import tut
from shop import shops
os.system('cls')

#WORLD STUFF YAH YAH
name = input("Please insert your name: ").title()
products = (["Gun", "Sword", "Healing-Potion", "Toy-Goblin"])

#LATER CREATE A CLASS THAT ALLOWS YOU TO ADD ATTACK DMG BY A CERTAIN AMOUNT IF YOU DO
coins = 200
HEALTH = 100
exp = 0
NPC = Merchant("MERCHANT", products)
Users = User(name, HEALTH, coins, [], exp)  
User_attack_dmg = 30
d = tut("Mr.Whalen")
fin_enemy_health = 1000

#create a function that allows the user to take out items and use it to attack.

d.tutorial()  
def after_tut():
     os.system('cls')
     fjji = input("Where would you like to go? SHOP/INVENTORY/BATTLE(Attack other enemies)/FINAL BATTLE: ").upper()
     if fjji == "SHOP":
          SHOP()
     if fjji == "BATTLE":
          BATTLE()
     if fjji == "FINAL BATTLE":
          FINAL_BATTLE()
     if fjji == "INVENTORY":
          inventory()
def shopping():
     
def inventory():
     show_inv = input(f"INVENTORY: {Users.inventory} ")
     equip = input("Would you like to equip anything? Y/N: ").upper()
     if equip == "N":
          input("Ok.. Returning to main screen...")
     if equip == "Y":
          item = input("What would you like to equip?").title()
          if item in Users.inventory:
               input(f"{item} is now equipped")
          if item not in Users.inventory:
               print("You're stupid as hell, you didn't type in an item you have you clown.")
     after_tut()
def BATTLE():
     Welcoming_to_BATTLE = input("You've entered the battle... press enter to continue..")
     type = random.randint(1,4)
     
     if type == 1:
          enemy_name, enemyhealth,enemy_dmg = "Dragon", 100, 27
     if type == 2:
          enemy_name, enemyhealth, enemy_dmg = "Zombie", 200, 32
     if type == 3:
          enemy_name, enemyhealth, enemy_dmg = "Skeletion", 250, 38
     if type == 4:
          enemy_name, enemyhealth, enemy_dmg = "dsauidiu", 400, 41


     enemy = ENEMY(enemy_name, enemyhealth)

     auhadsuai = input(f"YOU'VE ENCOUNTERED A {enemy_name}!")



     while enemy.hp >0 and Users.hp >0:
          BATTLE_IDK = input("Would you like to attack the enemy? press E to attack or L to leave: ").upper()
          if BATTLE_IDK == "E":
                    g = random.randint(1,6)
                    h = random.randint(1,6)
                    o = random.randint(1,6)
                    p = random.randint(1,6)
                    dh = Users.attack(g, p, enemy, User_attack_dmg)
                    print(enemy.hp)
                    uds = enemy.attack(o, h, Users, enemy_dmg)
                    print(Users.hp)
          if BATTLE_IDK == "L":
               print("You have left the battle...")
               Users.lose_EXP(10)
               after_tut()

     #i carry the group frsfrs    
def FINAL_BATTLE():
     if exp >= 100:
          reach_lvl = f"YOU'VE REACHED THE LEVEL TO BEAT THE FINAL BOSS..." 
     if exp < 100:
          not_high_enough_lvl = input("You are not high enough level.")
          returning_main = input("returning to main screen...")
          after_tut()

after_tut()


