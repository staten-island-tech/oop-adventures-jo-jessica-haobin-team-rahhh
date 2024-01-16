import random

class User:
    def __init__(self, name, hp, currency, inventory, exp, equipped_items):
        self.name = name
        self.hp = hp
        self.currency = currency
        self.inventory = inventory
        self.exp = exp
        self.equipped_items = []
    def buy(self, item):
        self.inventory.append(item)
        print(f"INVENTORY : {self.inventory}")
    def remove_currency(self, coins):
        self.currency -= coins
        print(f"COINS : {self.currency}")
    def sell(self, item):
        self.inventory.remove(item)
        print(f"INVENTORY : {self.inventory}")
    def add_currency(self, coins):
        self.currency += coins
        print(f"COINS : {self.currency}")
    def gain_EXP(self, experience_pts):
        self.exp += experience_pts
        print(f"LEVEL : {self.exp/100}")
    def lose_EXP(self, experience_pts):
        self.exp -= experience_pts
        print(f"LEVEL : {self.exp/100}")
    def gain_healths(self, health):
        self.hp += health
    def attack(self, dice_1, dice_2, enemy, attack_dmg):
        if dice_1 + dice_2 <= 6:
            print(f"You've rolled a {dice_1} and  {dice_2}. You are able to attack the enemy.")
            enemy.hp -= attack_dmg
        if dice_1 + dice_2 > 6:
            print(f"You've rolled a {dice_1} and {dice_2}. Your turn has been skipped...")
    def remove_item_from_equipped(self, item):
        if item in self.equipped_items:
            self.equipped_items.remove(item)
            input(f"Item {item} removed from equipped items.")
        else:
            input(f"{self.name} does not have {item} equipped.")

    def add_item_from_equipped(self, item):
        self.equipped_items.append(item)
        print(f"Equipped items: {self.equipped_items}")
        
    def equipping(self, item):
        if self.check_if_equipped(item):
            input(f"{self.name} already has {item} equipped.")
        else: 
            self.equipped_items.append(item)
            input(f"{self.name} equips {item}.")
    def check_if_any_equipped(self, excluded_item=None):
        for item in self.equipped_items:
            if item != excluded_item:
                return True
        return False
       
    
            
            



        