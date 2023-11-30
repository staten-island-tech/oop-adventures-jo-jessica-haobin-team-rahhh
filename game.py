from merchant import Merchant
from user import User
from enemy import Enemy

#WORLD STUFF YAH YAH
name = input("Please insert your name: ").title()
products = ["Gun", "Sword", "Healing-Potion", "Toy-Goblin"]
coins = 200
HEALTH = 100
type = input("Would you like to be a warrior or a mage?: ").upper()
NPC = Merchant("MERCHANT", products)
Users = User(name, HEALTH, coins, [], type)  

def tutorial():
     enemy_name = "Mr.Whalen"
     sukds = input("To continue to the instructions to this game, click enter.")
     dsoa = input("There was once a land which was ruled by kings and queens. The kingdom was at peace and everyone went along their way.")
     adi = input(f"Until one day they were attacked by a enemy who goes by {enemy_name}. He was feared throughout the years and until now he didn't attack.")
     usu = input(f"The kingdom was broken down and {enemy_name} took over the area. Houses were burned and people were turned into slaves.")
     hsdo = input(f"It is up to you, to defeat {enemy_name} and restore the kingdom.")
     items_given_by_me = input("You were given 200 coins to start with and 100 HP.")
     dsoh = input("Instructions: To attack, input E. To heal, input H. To engage in the fight, input P. To run away, input R. To equip your weapon or unequip your weapon, input E. ")
     fjji = input("Where would you like to go? SHOP/BATTLE: ").upper()
     if fjji == "SHOP":
          SHOP()
     if 



def SHOP():
     Welcoming_to_SHOP = input("Welcome to the SHOP! Would you like to sell items or buy them? BUY/SELL: ").upper()

     if Welcoming_to_SHOP == "BUY":
          for item in products:
               print(f'ITEM: {item}, AMOUNT: 100')               
          Buy = input("What item would you like to buy?: ").title()

          sd = NPC.sell(Buy)
          sad = Users.buy(Buy)
          sdh = Users.remove_currency(100)
     if Welcoming_to_SHOP == "SELL":
          sell = input("What item would you like to sell?: ")
          ahs = NPC.buy(sell)
          dhs = Users.sell(sell)
          dhsk = Users.add_currency(100)

def BATTLE():
     Welcoming_to_BATTLE = input("You've entered the battle... press enter to continue..")
     BATTLE_IDK = input("Would you like to attack the enemy? press E to attack: ").upper()









tutorial()