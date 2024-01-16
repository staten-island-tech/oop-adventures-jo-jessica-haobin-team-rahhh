import random, os, json
os.system('cls')

data = open("./data.json", encoding="utf8")
data = json.load(data)
character, stab, knife_throw = 100, random.randint(20, 40), random.randint(10,70)
fireball, laserbeam =  random.randint(30, 120), random.randint(50, 60)
def dialogue(Statements = '', Options = ''):    
    if Statements != '':
        for Statement in Statements: 
            print(Statement)
    if Options != '':
        Choices = input(f"{'|'.join(Options)}: ").capitalize()
        while Choices not in Options:
            Choices = input(f"{'|'.join(Options)}: ").capitalize()
        return Choices
    else: input(Options)
class partsinbattle:
    def spawn_enemy(b):
        global enemy_name
        if b > 90:
            enemy_name = 'Dragon'
            print("A Dragon spawned")
        elif b > 50:
            enemy_name = 'Zombie'
            print("A Zombie spawned")
        elif b > 30:
            enemy_name = 'Skeleton'
            print("A Skeleton spawned") 
        elif b >= 1:
            enemy_name = 'Goblin'
            print("A Goblin spawned")
        
    def warrior_fight(enemy_name):
        global character, stab, knife_throw
        if enemy_name == 'Dragon': enemy_name, enemy_attack, enemy_health = data[0]['Name'], data[0]['Damage'], data[0]['Health']
        elif enemy_name == 'Zombie': enemy_name, enemy_attack, enemy_health = data[2]['Name'], data[2]['Damage'], data[2]['Health']
        elif enemy_name == 'Skeleton': enemy_name, enemy_attack, enemy_health = data[3]['Name'], data[3]['Damage'], data[3]['Health']
        elif enemy_name == 'Goblin': enemy_name, enemy_attack, enemy_health = data[1]['Name'], data[1]['Damage'], data[1]['Health']
        elif enemy_name == 'Mr.Whalen': enemy_name, enemy_attack, enemy_health = data[4]['Name'], data[4]['Damage'], data[4]['Health']
        while True:
            os.system('cls')
            a, g = random.randint(1,6), random.randint(1,6)
            if a + g > 6: 
                Choices = dialogue([f"You've rolled a {a+g} so you can attack", "Choose between the following attacks"], ['Stab','Knife throw'])
                if Choices == 'Stab':
                    os.system('cls')
                    enemy_health -=stab
                    if  enemy_health <= 0: 
                        enemy_health = 0
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'])
                        return True
                    else: 
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '])
                elif Choices == 'Knife throw':
                    os.system('cls')
                    enemy_health -=knife_throw
                    if enemy_health <= 0:
                        enemy_health = 0
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'])
                        return True
                    else: 
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '])
                            
            elif a + g == 6:
                Choices = dialogue([f"You've rolled a {a+g} so you can choose to heal instead of attack", 'Choose between the following' ], ['Heal', 'Attack'])
                if Choices == 'Heal':
                    os.system('cls')
                    character += 100
                    dialogue([f"You've healed 100 hp. You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '])
                elif Choices == 'Attack':
                    os.system('cls')
                    print('Choose between the following')
                    dialogue(Options=['Stab', 'Knife throw'])
                    if  Choices == 'Stab':
                        enemy_health -=stab
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'])
                            return True
                        else: 
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '])
                    elif Choices == 'Knife throw':
                        os.system('cls')
                        enemy_health -=knife_throw
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'])
                            return True
                        else: 
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '])

            elif a + g < 6:
                os.system('cls')
                print(f"You've rolled {a+g} so the enemy hit you.")
                character -=enemy_attack
                if  character <= 0:
                    character = 0
                    os.system('cls')
                    dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You lost'])
                    return False
                else: 
                    dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '])

    def mage_fight(enemy_name):
        global character, fireball, laserbeam
        if enemy_name == 'Dragon': enemy_name, enemy_attack, enemy_health = data[0]['Name'], data[0]['Damage'], data[0]['Health']
        elif enemy_name == 'Zombie': enemy_name, enemy_attack, enemy_health = data[2]['Name'], data[2]['Damage'], data[2]['Health']
        elif enemy_name == 'Skeleton': enemy_name, enemy_attack, enemy_health = data[3]['Name'], data[3]['Damage'], data[3]['Health']
        elif enemy_name == 'Goblin': enemy_name, enemy_attack, enemy_health = data[1]['Name'], data[1]['Damage'], data[1]['Health']
        elif enemy_name == 'Mr.Whalen': enemy_name, enemy_attack, enemy_health = data[4]['Name'], data[4]['Damage'], data[4]['Health']
        while True:
            os.system('cls')
            a, g = random.randint(1,6), random.randint(1,6)
            if a + g > 7:
                Choices = dialogue([f"You've rolled a {a+g} so you can attack", "Choose between the following attacks"], ['Fireball', 'Laserbeam'])
                if Choices == 'Fireball':
                    os.system('cls')
                    enemy_health -=fireball
                    if  enemy_health <= 0:
                        enemy_health= 0
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'])
                        return True
                    else: 
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '])
                elif Choices == 'Laserbeam':
                    os.system('cls')
                    enemy_health -=laserbeam
                    if  enemy_health <= 0:
                        os.system('cls')
                        enemy_health = 0
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'])
                        return True
                    else: 
                        os.system('cls')
                        dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '])
                    
            elif a + g == 7:
                os.system('cls')
                Choices = dialogue([f"You've rolled a {a+g} so you can choose to heal instead of attack", 'Choose between the following' ], ['Heal', 'Attack'])
                if Choices == 'Heal':
                    os.system('cls')
                    character += 100
                    dialogue([f"You've healed 100 HP. You currently have {character} HP. Then {enemy_name} currently have {enemy_health} HP", 'Press any button to continue: '])
                elif Choices == 'Attack':
                    os.system('cls')
                    print('Choose between the following')
                    Choices = dialogue(Options=['Fireball', 'Laserbeam'])
                    if  Choices == 'Fireball':
                        os.system('cls')
                        enemy_health -=fireball
                        if  enemy_health <= 0:
                            os.system('cls')
                            enemy_health = 0
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'])
                            return True
                        else: 
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '])

                    elif Choices == 'Laserbeam':
                        enemy_health -=laserbeam
                        if  enemy_health <= 0:
                            enemy_health = 0
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You win'])
                            return True
                        else: 
                            os.system('cls')
                            dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'Press any button to continue: '])

            elif a + g < 7:
                os.system('cls')
                print(f"You've rolled {a+g} so the enemy hit you.")
                character -=enemy_attack
                if character <= 0:
                    character = 0
                    os.system('cls')
                    dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.", 'You lost'])
                    return False
                else: 
                    os.system('cls')
                    dialogue([f"You currently have {character} HP. The {enemy_name} currently have {enemy_health} HP.",'Press any button to continue: '])

def fight():
    b = random.randint(1,100)
    global enemy_health, enemy_attack, enemy_name
    os.system('cls')
    h = dialogue(['Choose between Warrior and Mage: '], ['Warrior', 'Mage'])
    os.system('cls')
    partsinbattle.spawn_enemy(b)
    dialogue([f"You are on an adventure and you encounter a {enemy_name}. The chances of you attacking and the enemy attacking is decided by 2 dices.", 'Press any buttons to continue to fight:  '])
    os.system('cls')
    if h == "Warrior":
        partsinbattle.warrior_fight(enemy_name)
        if partsinbattle.warrior_fight(enemy_name) == True:
            return True
        else: 
            return False
    elif h == "Mage":
        partsinbattle.mage_fight(enemy_name)
        if partsinbattle.mage_fight(enemy_name) == True:
            return True
        else: 
            return False
