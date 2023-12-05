from merchant import Merchant
from user import User
from enemy import ENEMY
import random
from tutorial import tut

#WORLD STUFF YAH YAH
name = input("Please insert your name: ").title()
products = ["Gun", "Sword", "Healing-Potion", "Toy-Goblin"]
coins = 200
HEALTH = 100
exp = 0
type = input("Would you like to be a warrior or a mage?: ").upper()
NPC = Merchant("MERCHANT", products)
Users = User(name, HEALTH, coins, [], type, exp)  
d = tut("Mr.Whalen")
fin_enemy_health = 1000

d.tutorial()


def after_tut():
     fjji = input("Where would you like to go? SHOP/BATTLE(Attack other enemies)/FINAL BATTLE: ").upper()
     if fjji == "SHOP":
          SHOP()
     if fjji == "BATTLE":
          BATTLE()
     if fjji == "FINAL BATTLE":
          FINAL_BATTLE()
after_tut()    
def SHOP():
     Welcoming_to_SHOP = input("Welcome to the SHOP! Would you like to sell items or buy them? BUY/SELL/LEAVE: ").upper()

     if Welcoming_to_SHOP == "BUY":
          for item in products:
               print(f'ITEM: {item}, AMOUNT: 100')               
          Buy = input("What item would you like to buy?: ").title()

          sd = NPC.sell(Buy)
          sad = Users.buy(Buy)
          sdh = Users.remove_currency(100)
          print("Thank you for shopping...")
          after_tut()
     if Welcoming_to_SHOP == "SELL":
          sell = input("What item would you like to sell?: ")
          ahs = NPC.buy(sell)
          dhs = Users.sell(sell)
          dhsk = Users.add_currency(100)
          print("Thank you for shopping...")
          after_tut()
     if Welcoming_to_SHOP == "LEAVE":
          print("Thank you for coming...")
          after_tut()
def BATTLE():
     Welcoming_to_BATTLE = input("You've entered the battle... press enter to continue..")
     type = random.randint(1,4)
     
     if type == 1:
          enemy_name = "Dragon"
          enemyhealth = 100 
     if type == 2:
          enemy_name = "Zombie"
          enemyhealth = 200
     if type == 3:
          enemy_name = "Skeletion"
          enemyhealth = 250
     if type == 4:
          enemy_name = "dad"
          enemyhealth = 400

     enemy = ENEMY(enemy_name, enemyhealth)

     auhadsuai = input(f"YOU'VE ENCOUNTERED A {enemy_name}!")
     BATTLE_IDK = input("Would you like to attack the enemy? press E to attack: ").upper()
     if BATTLE_IDK == "E":
          a = random.randint(1,6)
          g = random.randint(1,6)
          if a + g > 6:
               print(f"You've rolled a {a+g} so you can attack the enemy.")
               e = input("Choose between a stab or a knife throw: ").lower()

     #put haobins code grah     
def FINAL_BATTLE():
     if exp == 100:
          adsiuhd = f"YOU'VE REACHED THE LEVEL TO BEAT ." 

     