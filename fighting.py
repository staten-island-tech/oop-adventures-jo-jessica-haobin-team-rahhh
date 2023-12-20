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
    b = random.randint(1,100)
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

def dialogue(Statements = '', Options = ''):    
    if Statements != '':
        for Statement in Statements: 
            print(Statement)
    if Options != '':
        Choices = input(f"{'|'.join(Options)}: ").lower()
        while Choices not in Options:
            Choices = input(f"{'|'.join(Options)}: ").lower()
        return Choices
    else: input(Options)
    
def warrior_fight(warrior, enemy):
    global b
    global enemy_health, enemy_attack, enemy_name

    character, stab, knife_throw = warrior.health, warrior.stab, warrior.knife_throw
    while True:
        i = 1
        for i in range(i):
            i += 1
            os.system('cls')
            a, g = random.randint(1,6), random.randint(1,6)
            if a + g > 6: 
                Choices = dialogue([f"You've rolled a {a+g} so you can attack", "Choose between the following attacks"], ['stab','knife throw'])
                if Choices == 'stab':
                    os.system('cls')
                    enemy_health -=stab
                    if  enemy_health <= 0: 
                        enemy_health = 0
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'], [''])
                    else: 
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '], [''])
                elif Choices == 'knife throw':
                    os.system('cls')
                    enemy_health -=knife_throw
                    if enemy_health <= 0:
                        enemy_health = 0
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'], [''])
                    else: 
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '], [''])
                            
            elif a + g == 6:
                Choices = dialogue([f"You've rolled a {a+g} so you can choose to heal instead of attack", 'Choose between the following' ], ['heal', 'attack'])
                if Choices == 'heal':
                    os.system('cls')
                    character += 100
                    dialogue([f"You've healed 100 hp. You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '], [''])
                elif Choices == 'attack':
                    os.system('cls')
                    print('Choose between the following')
                    dialogue(['stab', 'knife throw'])
                    if  Choices == 'stab':
                        enemy_health -=stab
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'], [''])
                            return
                        else: 
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '], [''])
                    elif Choices == 'knife throw':
                        os.system('cls')
                        enemy_health -=knife_throw
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'], [''])
                        else: 
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '], [''])

            elif a + g < 6:
                os.system('cls')
                print(f"You've rolled {a+g} so the enemy hit you.")
                character -=enemy_attack
                if  character <= 0:
                    character = 0
                    os.system('cls')
                    dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You lost'], [''])
                else: 
                    dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '], [''])

def mage_fight(mage, enemy):
    global b
    global enemy_health, enemy_attack, enemy_name
    character, fireball, laserbeam = mage.health, mage.fireball, mage.laserbeam
    while True:
        i = 1
        for i in range(i):
            i += 1
            os.system('cls')
            a, g = random.randint(1,6), random.randint(1,6)
            if a + g > 7:
                Choices = dialogue([f"You've rolled a {a+g} so you can attack", "Choose between the following attacks"], ['fireball', 'laserbeam'])
                if Choices == 'fireball':
                    os.system('cls')
                    enemy_health -=fireball
                    if  enemy_health <= 0:
                        os.system('cls')
                        enemy_health= 0
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'], [''])
                        return
                    else: 
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '], [''])
                elif Choices == 'laserbeam':
                    os.system('cls')
                    enemy_health -=laserbeam
                    if  enemy_health <= 0:
                        os.system('cls')
                        enemy_health = 0
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'], [''])
                        return
                    else: 
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '], [''])
                    
            elif a + g == 7:
                os.system('cls')
                Choices = dialogue([f"You've rolled a {a+g} so you can choose to heal instead of attack", 'Choose between the following' ], ['heal', 'attack'])
                if Choices == 'heal':
                    os.system('cls')
                    character += 100
                    print(f"You've healed 100 HP. You currently have {character} HP. Then {enemy_name} currently have {enemy_health} HP")
                    input('Press any button to continue: ')
                elif Choices == 'attack':
                    os.system('cls')
                    print('Choose between the following')
                    Choices = dialogue([''],['fireball', 'laserbeam'])
                    if  Choices == 'fireball':
                        os.system('cls')
                        enemy_health -=fireball
                        if  enemy_health <= 0:
                            os.system('cls')
                            enemy_health = 0
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'], [''])
                            return
                        else: 
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '], [''])

                    elif Choices == 'laserbeam':
                        enemy_health -=laserbeam
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'], [''])
                            return
                        else: 
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '], [''])

            elif a + g < 7:
                os.system('cls')
                print(f"You've rolled {a+g} so the enemy hit you.")
                character -=enemy_attack
                if character <= 0:
                    character = 0
                    os.system('cls')
                    dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You lost'], [''])
                    return
                else: 
                    dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '], [''])


def fight(enemy, warrior, mage):
    global b 
    global enemy_health, enemy_attack, enemy_name
    os.system('cls')
    spawn_enemy(b)
    dialogue([f"You are on an adventure and you encounter a {enemy_name}. The chances of you attacking and the enemy attacking is decided by 2 dices.", 'Press any buttons to continue to fight:  '], [''])
    os.system('cls')
    if h == "warrior":
        warrior_fight(warrior, enemy)
    elif h == "mage":
        mage_fight(mage, enemy)
fight(enemy, warrior, mage)





