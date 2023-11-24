import random 

class user:
    def __init__(self, name:str, health:int, types:str):
        self.name = name
        self.health = health
        #health = 100 
        self.types = types

class warrior(user):
    def __init__(self, name:str, health:int, types:str, stab:int, knife_throw:int):
        super().__init__(name, health, types)
        self.stab = stab
        self.knife_throw = knife_throw
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.stab}, {self.types}, {self.knife_throw}"

class mage(user):
    def __init__(self, name:str, health:int, types:str, fireball:int, lazerbeam:int):
        super().__init__(name, health, types)
        self.fireball = fireball
        self.lazerbeam = lazerbeam
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.types}, {self.fireball}, {self.lazerbeam}"

class enemy(user):
    def __init__(self, name:str, health:int, types:str, damage:int ):
        super().__init__(name, health, types)
        self.damage = damage 
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.types}, {self.damage}"
    
class stuff_you_can_do(): 
    def attacks(self, attack, heal, start_fight):
        self.start_fight = start_fight
        start_fight = "P"
        self.attack = attack
        attack = "F"
        self.heal = heal
        heal = "H"


warrior = warrior("Deniz", 100, "melee", 20, 20)
mage = mage("Haobin", 100, "range", 20, 20)
enemy = enemy("goblin", 100, "melee", 20)


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
            lazerbeam = mage.lazerbeam
            y = int(mage.health**mage.health)
            for i in range(y):
                a = random.randint(1,6)
                g = random.randint(1,6)
                if a + g > 6:
                    print(f"You've rolled a {a+g} so you can attack.")
                    e = (input("Choose between fireball or lazerbeam: ")).lower()
                    if e == 'fireball':
                        enemy.health -=fireball
                    elif e == 'lazerbeam':
                        enemy.health -=lazerbeam
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



