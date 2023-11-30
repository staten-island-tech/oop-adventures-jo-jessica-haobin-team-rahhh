import random 
from realclasses import user, warrior, mage, enemy

class player:
    def __init__(self, health):
        self.health = health
    def createplayer():
        h = (input("Choose between Warrior and Mage: ")).lower()
        if h == "warrior":
            warrior.health = 100
            warrior.stab = 30
            warrior.knife_throw = 10
        elif h == "mage":
            mage.health = 150
            mage.fireball = 70
            mage.laserbeam = 50
    createplayer()

class battle:

    Dragon = enemy("Dragon", 300, "Hybrid", 60)
    Goblin = enemy("Goblin", 70, "Melee", 10)
    Zombie  = enemy("Zombie", 100, "Melee", 30)
    Skeleton = enemy("Skeleton", 90, "Range", 30)

    def fight(enemy, warrior, mage):
            global h
            Dragon = enemy("Dragon", 300, "Hybrid", 60)
            Goblin = enemy("Goblin", 70, "Melee", 10)
            Zombie  = enemy("Zombie", 100, "Melee", 30)
            Skeleton = enemy("Skeleton", 90, "Range", 30)
        
            
            b = random.randint(1,100)
            if b > 90:
                print("A Dragon spawned")
                enemy_attack = Dragon.damage
                enemy_name = Dragon.name
                enemy_health = Dragon.health
            elif b > 50:
                print("A Zombie spawned")
                enemy_attack = Zombie.damage
                enemy_name = Zombie.name
                enemy_health = Zombie.health
            elif b > 30:
                print("A Skeleton spawned") 
                enemy_attack = Skeleton.damage
                enemy_name = Skeleton.name
                enemy_health = Skeleton.health
            elif b > 1:
                print("A Goblin spawned")
                enemy_attack = Goblin.damage
                enemy_name = Goblin.name
                enemy_health = Goblin.health

            print(f"You are on an adventure and you encounter a {enemy_name}. The chances of you attacking and the enemy attacking is decided by 2 dices.")
            input('Press any buttons to continue to fight: ')
            if h == "warrior":
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
                            enemy_health -=stab
                            if  enemy_health <= 0:
                                enemy_health= 0
                            input('Press any buttons to continue: ')
                            print(f"You currently have {character} HP. The {enemy_name} currently have  {enemy_health} HP.")
                        elif e == 'knife throw':
                            enemy_health -=knife_throw
                            if  enemy_health <= 0:
                                enemy_health= 0
                            input('Press any buttons to continues: ')
                            print(f"You currently have {character} HP. The {enemy_name} currently have  {enemy_health} HP.")
                        input("Press any buttons to continues: ")
                    if character <= 0 and   enemy_health > 0:
                        print('You lost')
                        break
                    elif character > 0 and  enemy_health <= 0:
                        print('You win')
                        break
                        
                    elif a + g == 6:
                        print(f"You've rolled a {a+g}")
                        c = (input(f"You can choose to heal or choose to attack: ")).lower()
                        if c == 'heal':
                            character += 90
                            print(f"You've healed 90 HP. You currently have {character} HP. Then {enemy_name} currently have {enemy_health} HP")
                        elif c == 'attack':
                            c = (input("Choose between fireball or laserbeam: ")).lower()
                            if  c== 'fireball':
                                enemy_health -=stab
                                if  enemy_health <= 0:
                                    enemy_health= 0
                                print(f"You currently have {character} HP. The {enemy_name} currently have  {enemy_health} HP.")
                            elif c == 'laserbeam':
                                enemy_health -=knife_throw
                                if  enemy_health <= 0:
                                    enemy_health= 0
                    
                    elif a + g < 6:
                        print(f"You've rolled {a+g} so the enemy hit you.")
                        character -=enemy_attack
                        if  character <= 0:
                            character= 0
                        print(f"You currently have {character} HP. The {enemy_name} currently have  {enemy_health} HP.")
                        input("Press any buttons to continue: ")
                    if character <= 0 and   enemy_health > 0:
                        print('You lost')
                        break
                    elif character > 0 and  enemy_health <= 0:
                        print('You win')
                        break
                            

            elif h == "mage":
                character = mage.health
                fireball = mage.fireball 
                laserbeam = mage.laserbeam
                y = int(mage.health**mage.health)
                for i in range(y):
                    a = random.randint(1,6)
                    g = random.randint(1,6)
                    if a + g > 9:
                        print(f"You've rolled a {a+g} so you can attack.")
                        e = (input("Choose between fireball or laserbeam: ")).lower()
                        if e == 'fireball':
                            enemy_health -=fireball
                            if  enemy_health <= 0:
                                enemy_health= 0
                            print(f"You currently have {character} HP. The {enemy_name} currently have  {enemy_health} HP.")
                        elif e == 'laserbeam':
                            enemy_health -=laserbeam
                            if  enemy_health <= 0:
                                enemy_health= 0
                            print(f"You currently have {character} HP. The {enemy_name} currently have  {enemy_health} HP.")
                        input("Press any buttons to continues: ")
                    if character <= 0 and   enemy_health > 0:   
                        print('You lost')
                        break
                    elif character > 0 and  enemy_health <= 0:
                        print('You win')
                        break
                    
                    elif a + g == 9:
                        print(f"You've rolled a {a+g}")
                        c = (input(f"You can choose to heal or choose to attack: ")).lower()
                        if c == 'heal':
                            character += 90
                            print(f"You've healed 90 HP. You currently have {character} HP. Then {enemy_name} currently have {enemy_health} HP")
                        elif c == 'attack':
                            c = (input("Choose between fireball or laserbeam: ")).lower()
                            if  c== 'fireball':
                                enemy_health -=fireball
                                if  enemy_health <= 0:
                                    enemy_health= 0
                                print(f"You currently have {character} HP. The {enemy_name} currently have  {enemy_health} HP.")
                            elif c == 'laserbeam':
                                enemy_health -=laserbeam
                                if  enemy_health <= 0:
                                    enemy_health= 0

                    elif a + g < 9:
                        print(f"You've rolled {a+g} so the enemy hit you.")
                        character -=enemy_attack
                        if  character <= 0:
                            character = 0
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        input("Press any buttons to continue: ")
                    if character <= 0 and   enemy_health > 0:
                        print('You lost')
                        break
                    elif character > 0 and  enemy_health <= 0:
                        print('You win')
                        break
    fight(enemy, warrior, mage)



