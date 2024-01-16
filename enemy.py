class FINAL_ENEMY:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.POWER = power
    def GET_HIT(self, dmg):
        self.HP -= dmg
        print(f"ENEMY'S HEALTH : {self.HP}")
    
import random

class ENEMY:
    def __init__(self, name,  hp):
        self.name = name
        self.hp = hp
    def attack(self, dice_1, dice_2, user, enemy_dmg):
        if dice_1 + dice_2 <= 6:
            print(f"The enemy has rolled a {dice_1} and {dice_2}. The enemy has it's turn skipped...")
        if dice_1 + dice_2 > 6:
            print(f"The enemy has rolled a {dice_1} and {dice_2}. It attacks you.")
            user.hp -= enemy_dmg
            