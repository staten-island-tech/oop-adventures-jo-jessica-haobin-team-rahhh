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
            print(f"You've rolled a {a} so you can attack.")
            b = (input("Pick between stab, punch, fireball, or knife throw: ")).lower()
            if b == 'stab':
                enemy.health = stab
            elif b == 'punch':
                enemy.health = punch
            elif b == 'fireball':
                enemy.health = fireball
            elif b == 'knife throw':
                enemy.health = knife_throw
            print(f"You hit the enemy. You currently have {character} HP. The enemy currently have {enemy.health} HP")
            input('Press any buttons to continue: ')
        
        elif a == 6:
            print(f"You've rolled a {a} so you can choose to heal or attack.")
            c = (input("Do you choose to heal or attack: ")).lower()
            if c == 'heal':
                character = character + 20
                print(f"You've successfully healed. You currently have {character} HP. Then enemy currently have {enemy.health} HP")
                input('Press any buttons to continue: ')
            elif c == 'attack':
                b = (input("Pick between stab, punch, fireball, or knife throw: ")).lower()
                if b == 'stab':
                    enemy.health = stab
                elif b == 'punch':
                    enemy.health = punch
                elif b == 'fireball':
                    enemy.health == fireball
                elif b == 'knife throw':
                    enemy.health = knife_throw
                print(f"You've chose to attack. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
                input('Press any  buttons to continue: ')

        elif a < 6: 
            print(f"You've rolled a {a} so you missed.")
            character = enemy_attack
            print(f"The enemy hit you. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
            input('Press any buttons to continue: ')

        
        if character > 0 and enemy.health <= 0:
            print('You win')
        elif character > 0 and enemy.health > 0:
            fight(enemy)
        elif character <= 0 and enemy.health > 0:
            print('You lost')
        


fight(enemy)



