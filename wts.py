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
        
        
        if a > 6: 
            enemy.health = stab
        elif a < 6: 
            enemy.health = enemy.health
        print(f'You have rolled a {a}')

enemy = enemy(100, 20)

print(enemy.health)

