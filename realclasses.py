class user():
    def __init__(self, name:str, health:int, types:str):
        self.name = name
        self.health = health
        self.types =  types
        #health = 100

class enemy(user):
    def __init__(self, name:str, health:int, types:str, damage:int, weapon:str):
        super().__init__(name, health, types)
        self.damage = damage
        self.weapon = weapon
    def __str__(self):
        return f"{self.name}, {self.health}, {self.types}, {self.weapon}, {self.damage}"


class warrior(user):
    def __init__(self, name:str, health:int, types:str, weapon:str, warrior_skills:str):
        super().__init__(name, health, types)
        self.warrior_skills = warrior_skills
        self.weapon = weapon
        print("Name:",name,"Health:",health, "Types:" ,types, "Skills:" ,warrior_skills,)
        #warrior_skills are stab, throw knife, and punch
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.types}, {self.weapon} {self.warrior_skills}"

class mage(user):
    def __init__(self, name, health, types, weapon, mage_skills):
        super().__init__(health, name, types)
        self.mage_skills = mage_skills
        self.weapon = weapon
        print("Name:" ,name, "Health:" ,health, "Types:" ,types, "Skills:" ,mage_skills,)
        #mage_skills(with weapon equipped) are fireball, heal, and punch
    def __str__(self):
        return f"{self.name}, {self.health}, {self.types}, {self.weapon}, {self.mage_skills}"

class stuff_you_can_do():
    def __init__(self, start_fight, attack_or_buff, give_up, equip_or_unequip):
        self.start_fight = start_fight
        self.attack_or_buff = attack_or_buff
        self.give_up = give_up
        self.equip_or_unequip = equip_or_unequip
        if self.start_fight.lower() == "start fight":
            x = input("Would you like to attack/buff?")
        if x = 
            #not sure if user == warrior works
            if x.lower() == "yes" and user == warrior:
                y = input("Would you like to use stab, knife throw, or punch?(Buff not available for warriors.)")
            if x.lower() == "yes" and user == mage:
                y = input("Would you like to use fireball, punch, or heal?")
         

    
    
    
    
    
    
    
    
    
    

    def start_fight():
        # x = input(would you like to start the fight or give up?) -> main
        if x.lower() == "p":
            y = input("Would you like to attack, heal, or give up?")
        def attack_or_buff():
            #can only use if class is warrior
            if y.lower() == "attack" and user == warrior:
                input("Would you like to use stab, knife throw, or punch?")
            #can only use if class is mage
            if y.lower() == "attack" and user == mage:
                input("Would you like to use fireball, punch, or heal?")
    def give_up():
        if x.lower() == "L":
            print("You lose.")
    def equip_or_unequip():
        if 
    

        







        
#start_fight = "P"
#attack = "F"
#heal = "H"
#give_up = "L"
#equip/unequip = "E"


warrior("Jess", 100, "Berserker", "[Stab, Throw Knife]")
#code doesn't work