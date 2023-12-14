import random 
from realclasses import user, warrior, mage, enemy

Dragon = enemy("Dragon", 300, "Hybrid", 60) #xp 40
Goblin = enemy("Goblin", 70, "Melee", 10)   #xp 5
Zombie  = enemy("Zombie", 100, "Melee", 30) #xp 15
Skeleton = enemy("Skeleton", 90, "Range", 30) #xp 10
Mr_Whalen = enemy("Mr.Whalen", 1000, "Big Boss", 100) #xp 50000

class player:
    def __init__(self, health):
        self.health = health
    def createplayer():
        global h
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

global b 
b = random.randint(1,100)

def spawn_enemy(b):
    global enemy_attack, enemy_health, enemy_name 
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
    elif b >= 1:
        print("A Goblin spawned")
        enemy_attack = Goblin.damage
        enemy_name = Goblin.name
        enemy_health = Goblin.health

def warrior_fight(warrior, enemy):
    global b 
    global enemy_health, enemy_attack, enemy_name

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
                    enemy_health = 0
                    print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                    print('You win')
                    break
                else: 
                    print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                    input('Press any button to continue: ')
            elif e == 'knife throw':
                enemy_health -=knife_throw
                if enemy_health <= 0:
                    enemy_health = 0
                    print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                    print('You win')
                    break
                else: 
                    print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                    input('Press any button to continue: ')
                        
        elif a + g == 6:
            print(f"You've rolled a {a+g}")
            c = (input(f"You can choose to heal or choose to attack: ")).lower()
            if c == 'heal':
                character += 90
                print(f"You've healed 100 HP. You currently have {character} HP. Then {enemy_name} currently have {enemy_health} HP")
                input('Press any button to continue: ')
            elif c == 'attack':
                c = (input("Choose between fireball or laserbeam: ")).lower()
                if  c == 'stab':
                    enemy_health -=stab
                    if  enemy_health <= 0:
                        enemy_health = 0
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        print('You win')
                        break
                    else: 
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        input('Press any button to continue: ')
                elif c == 'knife throw':
                    enemy_health -=knife_throw
                    if  enemy_health <= 0:
                        enemy_health = 0
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        print('You win')
                        break
                    else: 
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        input('Press any button to continue: ')

        elif a + g < 6:
            print(f"You've rolled {a+g} so the enemy hit you.")
            character -=enemy_attack
            if  character <= 0:
                character = 0
                print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                print('You lost')
                break
            else: 
                print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                input('Press any button to continue: ')

def mage_fight(mage, enemy):
    global b
    global enemy_health, enemy_attack, enemy_name

    character = mage.health
    fireball = mage.fireball 
    laserbeam = mage.laserbeam
    y = int(mage.health**mage.health)
    for i in range(y):
        a = random.randint(1,6)
        g = random.randint(1,6)
        if a + g > 7:
            print(f"You've rolled a {a+g} so you can attack.")
            e = (input("Choose between fireball or laserbeam: ")).lower()
            if e == 'fireball':
                enemy_health -=fireball
                if  enemy_health <= 0:
                    enemy_health= 0
                    print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                    print('You win')
                    break
                else: 
                    print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                    input('Press any button to continue: ')
            elif e == 'laserbeam':
                enemy_health -=laserbeam
                if  enemy_health <= 0:
                    enemy_health = 0
                    print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                    print('You win')
                    break
                else: 
                    print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                    input('Press any button to continue: ')
                
                    
        elif a + g == 7:
            print(f"You've rolled a {a+g}")
            c = (input(f"You can choose to heal or choose to attack: ")).lower()
            if c == 'heal':
                character += 100
                print(f"You've healed 100 HP. You currently have {character} HP. Then {enemy_name} currently have {enemy_health} HP")
                input('Press any button to continue: ')
            elif c == 'attack':
                c = (input("Choose between fireball or laserbeam: ")).lower()
                if  c == 'fireball':
                    enemy_health -=fireball
                    if  enemy_health <= 0:
                        enemy_health = 0
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        print('You win')
                        break
                    else: 
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        input('Press any button to continue: ')

                elif c == 'laserbeam':
                    enemy_health -=laserbeam
                    if  enemy_health <= 0:
                        enemy_health = 0
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        print('You win')
                        break
                    else: 
                        print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                        input('Press any button to continue: ')

        elif a + g < 7:
            print(f"You've rolled {a+g} so the enemy hit you.")
            character -=enemy_attack
            if character <= 0:
                character = 0
                print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                print('You lost')
                break
            else: 
                print(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.")
                input('Press any button to continue: ')


def fight(enemy, warrior, mage):
    global b 
    global enemy_health, enemy_attack, enemy_name
    spawn_enemy(b)
    print(f"You are on an adventure and you encounter a {enemy_name}. The chances of you attacking and the enemy attacking is decided by 2 dices.")
    input('Press any buttons to continue to fight: ')
    if h == "warrior":
        warrior_fight(warrior, enemy)    
    elif h == "mage":
        mage_fight(mage, enemy)

fight(enemy,warrior,mage)



