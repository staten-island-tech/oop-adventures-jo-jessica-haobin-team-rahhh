class Enemy:
    def __init__(self, hp, power):
        self.HP = hp
        self.POWER = power
    def GET_HIT(self, dmg):
        self.HP -= dmg
        print(f"ENEMY'S HEALTH : {self.HP}")
    def TYPES_OF_ENEMIES(self, type):
        self.type = type
        