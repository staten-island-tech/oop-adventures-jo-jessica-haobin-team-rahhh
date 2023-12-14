import random


class User:
    def __init__(self, name, hp, currency, inventory, type, exp):
        self.name = name
        self.hp = hp
        self.currency = currency
        self.inventory = inventory
        self.type = type
        self.exp = exp
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
        print(f"EXP : {self.exp}")
    def gain_healths(self, health):
        self.hp += health
    def attack(self, dice_1, dice_2, enemy, attack_dmg):
        if dice_1 + dice_2 <= 6:
            print(f"You've rolled a {dice_1 + dice_2}. Your turn has been skipped...")
            self.attack_dmg = attack_dmg
            enemy.hp -= self.attack_dmg
        if dice_1 + dice_2 > 6:
            print(f"You've rolled a {dice_1 + dice_2}. You are able to attack the enemy.")
            
            
            



        