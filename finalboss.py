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
    
    def sayyourclass():
        a = input("State your class one last time: ")
        return a

    def fightboss(yourclass):
        b = thebossbattle.createboss()
        if yourclass == 'warrior':
            a = partsinbattle.warrior_fight(b)
            if a == True:
                print('Congratulation of beating the boss!!!')
                return True
            elif a == False:
                print('You now have to start from scratch again.')
        elif yourclass == 'mage':
            c = partsinbattle.mage_fight(b)
            if c == True:
                print('Congratulation of beating the boss!!!')
            elif c == False:
                print('You now have to start from scratch again.')



