import random, os
from realclasses import user, warrior, mage, enemy
import json
os.system('cls')

data = open("./data.json", encoding="utf8")
data = json.load(data)
class player:
    def __init__(self, health):
        self.health = health
    def createplayer():
        global h
        h = (input("Choose between Warrior and Mage: ")).lower()
        if h == "warrior":
            warrior.health, warrior.stab, warrior.knife_throw = 100, 30, 10
        elif h == "mage":
            mage.health, mage.fireball, mage.laserbeam = 150, 70, 50
    createplayer()



global b 
b = random.randint(1,100)

def spawn_enemy(b):
    global enemy_attack, enemy_health, enemy_name 
    if b > 90:
        print("A Dragon spawned")
        enemy_name, enemy_attack, enemy_health = data[0]['Name'], data[0]['Damage'], data[0]['Health']
    elif b > 50:
        print("A Zombie spawned")
        enemy_name, enemy_attack, enemy_health = data[2]['Name'], data[2]['Damage'], data[2]['Health']
    elif b > 30:
        print("A Skeleton spawned") 
        enemy_name, enemy_attack, enemy_health = data[3]['Name'], data[3]['Damage'], data[3]['Health']
    elif b >= 1:
        print("A Goblin spawned")
        enemy_name, enemy_attack, enemy_health = data[1]['Name'], data[1]['Damage'], data[1]['Health']

def win_or_lose_statements(a, b):
    print(a)
    print(b)
def continuation_statements(a, b):
    print(a)
    input(b)

def warrior_fight(warrior, enemy):
    global b 
    global enemy_health, enemy_attack, enemy_name

    i = 1
    character, stab, knife_throw = warrior.health, warrior.stab, warrior.knife_throw
    while True:
        i += 1
        for i in range(i):
            os.system('cls')
            a, g = random.randint(1,6), random.randint(1,6)
            if a + g > 6: 
                print(f"You've rolled a {a+g} so you can attack.")
                e = (input("Choose between stab or knife throw: ")).lower()
                if e == 'stab':
                    os.system('cls')
                    enemy_health -=stab
                    if  enemy_health <= 0: 
                        enemy_health = 0
                        win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win')
                        return
                    else: 
                        os.system('cls')
                        continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')
                elif e == 'knife throw':
                    os.system('cls')
                    enemy_health -=knife_throw
                    if enemy_health <= 0:
                        enemy_health = 0
                        os.system('cls')
                        win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win')
                        return
                    else: 
                        os.system('cls')
                        continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')
                            
            elif a + g == 6:
                print(f"You've rolled a {a+g}")
                c = (input(f"You can choose to heal or choose to attack: ")).lower()
                if c == 'heal':
                    os.system('cls')
                    character += 100
                    continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')
                elif c == 'attack':
                    os.system('cls')
                    c = (input("Choose between stab or knife throw: ")).lower()
                    if  c == 'stab':
                        enemy_health -=stab
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win')
                            return
                        else: 
                            os.system('cls')
                            continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')
                    elif c == 'knife throw':
                        os.system('cls')
                        enemy_health -=knife_throw
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win')
                            return
                        else: 
                            os.system('cls')
                            continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')

            elif a + g < 6:
                os.system('cls')
                print(f"You've rolled {a+g} so the enemy hit you.")
                character -=enemy_attack
                if  character <= 0:
                    character = 0
                    os.system('cls')
                    win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You lost')
                    return
                else: 
                    continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')

def mage_fight(mage, enemy):
    global b
    global enemy_health, enemy_attack, enemy_name
    i = 1
    character, fireball, laserbeam = mage.health, mage.fireball, mage.laserbeam
    while True:
        i += 1
        for i in range(i):
            os.system('cls')
            a, g = random.randint(1,6), random.randint(1,6)
            if a + g > 7:
                print(f"You've rolled a {a+g} so you can attack.")
                e = (input("Choose between fireball or laserbeam: ")).lower()
                if e == 'fireball':
                    os.system('cls')
                    enemy_health -=fireball
                    if  enemy_health <= 0:
                        os.system('cls')
                        enemy_health= 0
                        win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win')
                        return
                    else: 
                        continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')
                elif e == 'laserbeam':
                    os.system('cls')
                    enemy_health -=laserbeam
                    if  enemy_health <= 0:
                        os.system('cls')
                        enemy_health = 0
                        win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win')
                        return
                    else: 
                        os.system('cls')
                        continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')
                    
                        
            elif a + g == 7:
                os.system('cls')
                print(f"You've rolled a {a+g}")
                c = (input(f"You can choose to heal or choose to attack: ")).lower()
                if c == 'heal':
                    os.system('cls')
                    character += 100
                    print(f"You've healed 100 HP. You currently have {character} HP. Then {enemy_name} currently have {enemy_health} HP")
                    input('Press any button to continue: ')
                elif c == 'attack':
                    os.system('cls')
                    c = (input("Choose between fireball or laserbeam: ")).lower()
                    if  c == 'fireball':
                        os.system('cls')
                        enemy_health -=fireball
                        if  enemy_health <= 0:
                            os.system('cls')
                            enemy_health = 0
                            win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win')
                            return
                        else: 
                            os.system('cls')
                            continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')

                    elif c == 'laserbeam':
                        enemy_health -=laserbeam
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win')
                            return
                        else: 
                            os.system('cls')
                            continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')

            elif a + g < 7:
                os.system('cls')
                print(f"You've rolled {a+g} so the enemy hit you.")
                character -=enemy_attack
                if character <= 0:
                    character = 0
                    os.system('cls')
                    win_or_lose_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You lost')
                    return
                else: 
                    continuation_statements(f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: ')


def fight(enemy, warrior, mage):
    global b 
    global enemy_health, enemy_attack, enemy_name
    os.system('cls')
    spawn_enemy(b)
    print(f"You are on an adventure and you encounter a {enemy_name}. The chances of you attacking and the enemy attacking is decided by 2 dices.")
    input('Press any buttons to continue to fight: ')
    os.system('cls')
    if h == "warrior":
        warrior_fight(warrior, enemy)
    elif h == "mage":
        mage_fight(mage, enemy)

fight(enemy,warrior,mage)



