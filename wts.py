import random 

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


print(enemy.health, character)