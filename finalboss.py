from fighting import partsinbattle
import os, json
data = open("./data.json", encoding="utf8")
data = json.load(data)
os.system('cls')


class thebossbattle:
    def createboss():
        enemy_name = 'Mr.Whalen'
        os.system('cls')
        print('This is the final battle!!! The monster Mr.Whalen is scary and dangerous!!! His head lights up the room with ominous white light!!! Beware and be prepare!!!')
        input("If you're still willing to continue press any buttons to go on: ")
        return enemy_name
    
    def chancetochangeclass():
        os.system('cls')
        print("You have a chance to change class before your battle! ")
        print("If you want to change class, choose the opposite of your current class")
        print("If you don't want to change class, choose the same class")
        Options = ['Warrior', 'Mage']
        if Options != '':
            x = input(f"{'|'.join(Options)}: ").capitalize()
            while x not in Options:
                x = input(f"{'|'.join(Options)}: ").capitalize()
            return x

    def fightboss(yourclass):
        os.system('cls')
        b = thebossbattle.createboss()
        if yourclass == 'Warrior':
            a = partsinbattle.warrior_fight(b)
            if a == True:
                print('Congratulation on beating the boss!!!')
                return True
            elif a == False:
                print('You now have to start from scratch again.')
        elif yourclass == 'Mage':
            c = partsinbattle.mage_fight(b)
            if c == True:
                print('Congratulation on beating the boss!!!')
            elif c == False:
                print('You now have to start from scratch again.')



