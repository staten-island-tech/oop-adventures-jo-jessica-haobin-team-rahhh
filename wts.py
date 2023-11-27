import random 

class enemy():
    def __init__(self, health:int, damage:int ):
        self.health = health 
        self.damage = damage 

character = 100
enemy = enemy(100, 20)

def fight(enemy):
    global character
    stab = 30 
    punch = 5 
    fireball = 50 
    knife_throw = 10
    enemy_attack = character - enemy.damage
    
    a = random.randint(1,12)
    
    if a > 6: 
        print(f'You have rolled a {a}')
        print(f"Your attack will have a 100% chance of hitting.")
        b = input("Choose between the attacks of stab, punch, fireball, or knife throw. You can choose to enhance your attacks. If the enhance fails the enemy deals more damage: ").lower()
        if b == ('stab'):
            enemy.health = enemy.health - stab
            print(f"You've attacked the enemy. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
        elif b == ('punch'):
            enemy.health = enemy.health - punch
            print(f"You've attacked the enemy. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
        elif b == ('fireball'):
            enemy.health = enemy.health - fireball
            print(f"You've attacked the enemy. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
        elif b == ('knife throw'):
            enemy.health = enemy.health - knife_throw
            print(f"You've attacked the enemy. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
        elif b == ('enhance'):
            c = random.randint(1,6)
            if c == 1:
                d = (input('Choose an attack to enhance: ')).lower
                if d == 'stab':
                    stab = 1.5 * stab
                    enemy.health = enemy.health - stab
                if d == 'punch':
                    punch = 1.5 * punch
                    enemy.health = enemy.health - punch
                if d == 'fireball':
                    fireball = 1.5 * fireball
                    enemy.health = enemy.health - fireball
                if d == 'knife throw':
                    knife_throw = 1.5 * knife_throw
                    enemy.health = enemy.health - knife_throw
                print(f"You've successfully enhanced your skill and attacked your enemy. You currently have {character} HP. The enemy currently have {enemy.health} HP.")

            elif c != 1:
                enemy_attack == 2 * enemy.damage
                character = character - enemy_attack
                print(f"You've failed to enhance your skill and the enemy attacked you with an enhanced attack. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
        input('Press any button to continue: ')

    elif a == 6:
        a = input('You have this chance to heal or continue fighting. If you would like to heal press H and if you would like to attack press G: ')
        if a == 'H':
            character = character + 20
            print(f"You've healed 20 HP. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
        elif a == 'G':
            enemy.health = enemy.health - 20
            print(f"You've attacked the enemy. You currently have {character} HP. The enemy currently have {enemy.health} HP.")
        

    elif a < 6: 
            print(f'You have rolled a {a}')
            character = character - enemy_attack
            print(f'Your attack missed so the enemy hit you. You currently have {character} HP. The enemy have {enemy.health} HP.')
            input("Press any button to continue playing: ")

    if character > 0 and enemy.health <= 0:
        print(f"You win. The enemy died. You have {character} health remaining")
    elif character > 0 and enemy.health > 0:
        print("Continue fighting")
    elif character <= 0 and enemy.health > 0:
        print(f"You lost. You died. The enemy have {enemy.health} health remaining")
    
fight(enemy)



