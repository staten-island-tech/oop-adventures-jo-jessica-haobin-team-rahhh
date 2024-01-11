from merchant import Merchant
from User import User
from enemy import ENEMY
import random, os
from tutorial import tut
import traceback
os.system('cls')

#WORLD STUFF YAH YAH
name = input("Please insert your name: ").title()
products = ["Gun", "Sword", "Axe", "Hammer"]


#LATER CREATE A CLASS THAT ALLOWS YOU TO ADD ATTACK DMG BY A CERTAIN AMOUNT IF YOU DO
coins = 200
HEALTH = 100
exp = 0
NPC = Merchant("MERCHANT", products)
Users = User(name, HEALTH, coins, [], exp, [])  
User_attack_dmg = 30
d = tut("Mr.Whalen")
fin_enemy_health = 1000
equipped = False

#create a function that allows the user to take out items and use it to attack.

""" d.tutorial()  """ 
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
     else: 
          input("clowner misspelled 🤡 ")
          after_tut()

     
def SHOP():
     os.system('cls')
     Welcoming_to_SHOP = input("Welcome to the SHOP! Would you like to sell items or buy them? BUY/SELL/LEAVE: ").upper()

     if Welcoming_to_SHOP == "BUY":
          for item in products:
               print(f'ITEM: {item}, AMOUNT: 100')               
          Buy = input("What item would you like to buy?: ").title()

          if Buy in products:
               if Users.currency <= 0:
                    no_money_bozo = input("Error... You do not have enough...")
                    return_to_tut = input("returning to main...")
               if Users.currency > 0:
                    merchant_sells = NPC.sell(Buy)
                    user_buys = Users.buy(Buy)
                    user_remove_buddys_currency_so_he_becomes_Broke_ash = Users.remove_currency(100)
                    return_to_tut = input("Thank you for shopping...")
                    os.system('cls')
                 
          else: 
               input("clowner misspelled 🤡 ")
    
          
     if Welcoming_to_SHOP == "SELL":
          sell = input("What item would you like to sell? If you would like to leave press L: ").title()
          if sell == "L":
               return_to_tut = input("returning to shop....")
        
          if sell in Users.inventory:
               print(Users.inventory)
               add_merchant_item = NPC.buy(sell)
               subtract_users_item = Users.sell(sell)
               add_money = Users.add_currency(100)
               return_to_tut = input("Thank you for shopping...")
        
          else: 
               input("clowner misspelled 🤡 ")
               SHOP()
          os.system('cls')
     if Welcoming_to_SHOP == "LEAVE":
          print("Thank you for coming...")
          after_tut()
     after_tut()
def inventory():
     show_inv = input(f"INVENTORY: {Users.inventory} ")
     equip = input("Would you like to equip anything? Y/N: ").upper()
     if equip == "N":
          check_equip = input("Would you like to check your equipped items? Y/N: ").upper()
          if check_equip == "Y":
               input(f"Equipped: {Users.equipped}")
          input("Ok.. Returning to main screen...")
          after_tut()
     if equip == "Y":
          buddy_wanna_equip = input("What would you like to equip?: ").title()
          if buddy_wanna_equip in Users.inventory:
               Users.add_item_from_equipped(buddy_wanna_equip, Users)
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


#maybe needed to put the items into catagory in healing, attacking, or buff potions. 