

class user():
    def character(self, name, health, types, ):
        self.name = name
        self.health = health
        #health = 100 
        self.type = types

class warrior(user):
    def __init__(self, name, health, types, stab, knife_throw):
        super().__init__(name, health, types)
        self.stab = stab
        self.knife_throw = knife_throw
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.stab}, {self.types}, {self.knife_throw}"

class mage(user):
    def __init__(self, name, health, types, fireball, heal):
        super().__init__(name, health, types)
        self.fireball = fireball
        self.heal = heal
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.fireball}, {self.types}, {self.heal}"

class stuff_you_can_do(): 
    def attacks(self, attack, heal, start_fight):
        self.start_fight = start_fight
        start_fight = "P"
        self.attack = attack
        attack = "F"
        self.heal = heal
        heal = "H"

def work_on_this_later():
    import random
    a = random.randint(1,12)  
    successful = (7,8,9,10,11,12)
    unsuccessful = (1,2,3,4,5,6)

    roll_the_dice = "yes"

    while roll_the_dice == "yes":
        roll_the_dice = input("would you like to roll the dice to see if you get a successful attack or not?: ").lower()
        if a in successful:
            print ("your attack was successful, 20 HP was taken away from the enemy")
            # put enemy's health - 20 after you get haobins code
            break
        if a in unsuccessful:
            print ("your attack was unsuccessful")
            break


 





