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
        def stab():
            self.hp -= stab
        def knife_throw():
            self.hp -= knife_throw
        def 
            