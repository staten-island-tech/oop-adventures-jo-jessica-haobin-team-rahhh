class FINAL_ENEMY:
    def __init__(self, name, hp, power):
        self.name = name
        self.HP = hp
        self.POWER = power
    def GET_HIT(self, dmg):
        self.HP -= dmg
        print(f"ENEMY'S HEALTH : {self.HP}")
    
import random

class ENEMY:
    def __init__(self, name,  hp):
        self.name = name
        self.hp = hp
    def fight(self, stab, knife_throw):
        stab = 100
        knife_throw = 50
        a = random.randint(1,6)
        g = random.randint(1,6)
        if a + g > 6:
            print(f"You've rolled a {a+g} so you can attack the enemy.")
            e = input("Choose between a stab or a knife throw: ").lower()
            if e == 'stab':
                self.hp -= stab
        