import random 
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


fight(enemy)
print(enemy.health, character)



