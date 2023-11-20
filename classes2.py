import random

class user():
    def character(self, name, health, types):
        self.name = name
        self.health = health
        #health = 100 
        self.type = types

class warrior(user):
    def __init__(self, name, health, types, stab, knife_throw):
        super().__init__(name, health, types)
        self.stab = stab
        self.knife_throw = knife_throw
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.stab}, {self.types}, {self.knife_throw}"

class mage(user):
    def __init__(self, name, health, types, fireball, heal):
        super().__init__(name, health, types)
        self.fireball = fireball
        self.heal = heal
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.fireball}, {self.types}, {self.heal}"

class stuff_you_can_do(): 
    def attacks(self, attack, heal, start_fight):
        self.start_fight = start_fight
        start_fight = "P"
        self.attack = attack
        attack = "F"
        self.heal = heal
        heal = "H"

class enemy():
    def __init__(self, health:int, damage:int ):
        self.health = health 
        self.damage = damage 

    character = 100

    def fight(self):
        global character
        stab = enemy.health - 20 
        punch = enemy.health - 20 
        fireball = enemy.health - 20 
        knife_throw = enemy.health - 20
        enemy_attack = character - enemy.attack

        a = random.randint(1,12)
        print(f'You have rolled a {a}')
        
        if a > 6: 
            b = input("Pick between stab, punch, fireball, or knife throw: ")
            if b == 'stab':
                enemy.health = stab
            elif b == 'punch':
                enemy.health = punch
            elif b == 'fireball':
                enemy.health = fireball
            elif b == 'knife throw':
                enemy.health = knife_throw
        elif a < 6: 
            character = enemy_attack

enemy = enemy(100, 20)