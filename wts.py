import random 

class enemy():
    
    def __init__(self, monster_name:str, health:int, damage:int ):
        self.monster_name = monster_name
        self.health = health 
        self.damage = damage 



class user():
    def character(self, name:str, health:int, types:str):
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

class stuff_you_can_do(): 
    def attacks(self, attack, heal, start_fight):
        self.start_fight = start_fight
        start_fight = "P"
        self.attack = attack
        attack = "F"
        self.heal = heal
        heal = "H"


warrior = warrior("Deniz", 100000000, "melee", 100, 100)
mage = mage("Haobin", 100000, "range", 100, 100)
enemy = enemy("goblin", 10000, 20)


def fight(enemy, warrior, mage):
        d = (input("Are you a warrior or mage?: ")).lower()
        if d == "warrior":
            character = warrior.health 
            stab = warrior.stab 
            knife_throw = warrior.knife_throw
        elif d == "mage":
            fireball = mage.fireball 
            lazerbeam = mage.lazerbeam
        enemy_attack = enemy.damage

        a = random.randint(1,6)
        g = random.randint(1,6)
        
        if a+g > 6: 
            print(f"You've rolled a {a+g} so you can attack.")
            if d == "warrior":
                e = (input("Choose between stab or knife throw: ")).lower()
                if e == 'stab':
                    enemy.health == enemy.health - stab
                elif e == 'knife throw':
                    enemy.health == enemy.health - knife_throw
            elif d == 'mage':
                f = (input('Choose between fireball or lazerbeam: ')).lower()
                if f == "fireball":
                    enemy.health == enemy.health - fireball
                elif f == "lazerbeam":
                    enemy.health == enemy.health - lazerbeam
            input(f"Press any button to continue: ")

        elif a+g == 6:
            print(f"You've rolled a {a+g} so you can choose to heal or attack.")
            c = (input("Do you choose to heal or attack: ")).lower()
            if c == 'heal':
                character = character + 20
                print(f"You've successfully healed. You currently have {character} HP. Then enemy currently have {enemy.health} HP")
                input('Press any buttons to continue: ')
            elif c == 'attack':
                b = (input("Pick between stab, punch, fireball, or knife throw: ")).lower()
                if b == 'stab':
                    enemy.health = enemy.health - stab
                elif b == 'fireball':
                    enemy.health == enemy.health - fireball
                elif b == 'knife throw':
                    enemy.health = enemy.health - knife_throw
                print(f"You've chose to attack. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
                input('Press any buttons to continue: ')

        elif a+g < 6: 
            print(f"You've rolled a {a+g} so you missed.")
            character = character - enemy_attack
            print(f"The enemy hit you. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
            input('Press any buttons to continue: ')

        
        if character > 0 and enemy.health <= 0:
            print('You win')
        elif character <= 0 and enemy.health > 0:
            print('You lost')
        elif character > 0 and enemy.health > 0:
            fight(enemy)


fight(enemy, warrior, mage)



