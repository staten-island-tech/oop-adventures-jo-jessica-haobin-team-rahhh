import os
from merchant import Merchant
from user import User
class shops():
     def __init__(self, products):
          self.products = products
     def SHOP(self):
        os.system('cls')
        Welcoming_to_SHOP = input("Welcome to the SHOP! Would you like to sell items or buy them? BUY/SELL/LEAVE: ").upper()

        if Welcoming_to_SHOP == "BUY":
            for item in self.products:
                print(f'ITEM: {item}, AMOUNT: 100')               
            Buy = input("What item would you like to buy?: ").title()

            if Users.currency > 0:
               merchant_sells = NPC.sell(Buy)
               user_buys = Users.buy(Buy)
               user_remove_buddys_currency_so_he_becomes_Broke_ash = Users.remove_currency(100)
               return_to_tut = input("Thank you for shopping...")
               
               os.system('cls')
          if Users.currency <= 0:
               no_money_bozo = input("Error... You do not have enough...")
               return_to_tut = input("returning to main...")
               SHOP()
     if Welcoming_to_SHOP == "SELL":
          sell = input("What item would you like to sell? If you would like to leave press L: ").title()
          if sell == "L":
               return_to_tut = input("returning to shop....")
               SHOP()
          if sell in Users.inventory:
               print(Users.inventory)
               add_merchant_item = NPC.buy(sell)
               subtract_users_item = Users.sell(sell)
               add_money = Users.add_currency(100)
               return_to_tut = input("Thank you for shopping...")
               SHOP()
          os.system('cls')
     if Welcoming_to_SHOP == "LEAVE":
          print("Thank you for coming...")
          after_tut()
     else: 
          input("clowner misspelled 🤡")
          SHOP()