import random
class User:
    def __init__(self, name, hp, currency, inventory, exp, equipped_items):
        self.name = name
        self.hp = hp
        self.currency = currency
        self.inventory = inventory
        self.exp = exp
        self.equipped = equipped_items
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
        self.equipped.remove(item)
    def add_item_from_equipped(self, item):
        self.equipped.append(item)
    
            
            



        