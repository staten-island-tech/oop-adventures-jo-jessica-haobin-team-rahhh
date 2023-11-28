import random 
from realclasses import user, warrior, mage, enemy

class player:
    def __init__(self, health):
        self.health = health
    def createplayer(self, health, classes):
        a = (input("Choose between Warrior and Mage")).lower()
        if a == "warrior":
            warrior.health = 100
            warrior.stab = 20
            warrior.knife_throw = 20
        elif a == "mage":
            mage.health = 100
            mage.fireball = 20
            mage.laserbeam = 20
            
class battle:

    def fight(enemy, warrior, mage):
            d = (input("Are you a warrior or mage?: ")).lower()
            enemy_attack = enemy.damage
            print(f"You are on an adventure and you encounter a {enemy.name}. The chances of you attacking and the enemy attacking is decided by 2 dices.")
            input('Press any buttons to continue to fight: ')
            if d == "warrior":
                character = warrior.health 
                stab = warrior.stab 
                knife_throw = warrior.knife_throw
                x = int(warrior.health**warrior.health)
                for i in range(x):
                    a = random.randint(1,6)
                    g = random.randint(1,6)
                    if a + g > 6: 
                        print(f"You've rolled a {a+g} so you can attack.")
                        e = (input("Choose between stab or knife throw: ")).lower()
                        if e == 'stab':
                            enemy.health -=stab
                            input('Press any buttons to continue: ')
                        elif e == 'knife throw':
                            enemy.health -=knife_throw
                            input('Press any buttons to continues: ')
                        print(f"You currently have {character} HP. The {enemy.name} currently have {enemy.health} HP.")
                        input("Press any buttons to continues: ")
                    if character == 0 and enemy.health > 0:
                        print('You lost')
                        break
                    elif character > 0 and enemy.health == 0:
                        print('You win')
                        break
                        

                    elif a + g < 6:
                        print(f"You've rolled {a+g} so the enemy hit you.")
                        character -=enemy_attack
                        print(f"You currently have {character} HP. The {enemy.name} currently have {enemy.health} HP.")
                        input("Press any buttons to continue: ")
                    if character == 0 and enemy.health > 0:
                        print('You lost')
                        break
                    elif character > 0 and enemy.health == 0:
                        print('You win')
                        break
                            

            elif d == "mage":
                character = mage.health
                fireball = mage.fireball 
                laserbeam = mage.laserbeam
                y = int(mage.health**mage.health)
                for i in range(y):
                    a = random.randint(1,6)
                    g = random.randint(1,6)
                    if a + g > 6:
                        print(f"You've rolled a {a+g} so you can attack.")
                        e = (input("Choose between fireball or laserbeam: ")).lower()
                        if e == 'fireball':
                            enemy.health -=fireball
                        elif e == 'laserbeam':
                            enemy.health -=laserbeam
                        print(f"You currently have {character} HP. The {enemy.name} currently have {enemy.health} HP.")
                        input("Press any buttons to continues: ")
                    if character == 0 and enemy.health > 0:
                        print('You lost')
                        break
                    elif character > 0 and enemy.health == 0:
                        print('You win')
                        break
                        
                        
                    elif a + g < 6:
                        print(f"You've rolled {a+g} so the enemy hit you.")
                        character -=enemy_attack
                        print(f"You currently have {character} HP. The {enemy.name} currently have {enemy.health} HP.")
                        input("Press any buttons to continue: ")
                    if character == 0 and enemy.health > 0:
                        print('You lost')
                        break
                    elif character > 0 and enemy.health == 0:
                        print('You win')
                        break
                        
                
                
    fight(enemy, warrior, mage)



