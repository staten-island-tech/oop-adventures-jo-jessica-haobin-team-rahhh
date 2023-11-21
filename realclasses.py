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

character = 100
class enemy():
    global character
    def __init__(self, health:int, damage:int ):
        self.health = health 
        self.damage = damage 

enemy = enemy(100, 20)

def fight(enemy):
        global character
        stab = enemy.health - 20 
        punch = enemy.health - 20 
        fireball = enemy.health - 20 
        knife_throw = enemy.health - 20
        enemy_attack = character - enemy.damage

        a = random.randint(1,12)
        
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

        elif a < 7: 
            print(f"You've rolled a {a} so you missed")
            character = enemy_attack
            print(character.health)

        
        if character > 0 and enemy.health == 0:
            print('gg')
        elif character == 0 and enemy.health > 0:
            print('play again')
        elif character > 0 and enemy.health > 0:
            fight(enemy)