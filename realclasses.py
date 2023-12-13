class user():
    def __init__(self, name:str, health:int, types:str):
        self.name = name
        self.health = health
        self.types =  types
        #health = 100
#this is a substitute for josephine's code

class warrior(user):
    def __init__(self, name:str, health:int, types:str, warrior_weapon:str, warrior_skills:str):
        super().__init__(name, health, types)
        self.warrior_skills = warrior_skills
        self.weapon = warrior_weapon
        print("Name:",name,"Health:",health, "Types:" ,types, "Weapon:" ,warrior_weapon, "Warrior Skills" ,warrior_skills,)
        #warrior_skills are stab, throw knife, and punch
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.types}, {self.weapon} {self.warrior_skills}"

class mage(user):
    def __init__(self, name:str, health:int, types:str, mage_weapon:str, mage_skills:str):
        super().__init__(health, name, types)
        self.mage_skills = mage_skills
        self.weapon = mage_weapon
        print("Name:" ,name, "Health:" ,health, "Types:" ,types, "Weapon:" ,mage_weapon, "Skills:" ,mage_skills,)
        #mage_skills are fireball, lazerbeam, heal, and punch
    def __str__(self):
        return f"{self.name}, {self.health}, {self.types}, {self.weapon}, {self.mage_skills}"
    
class type(mage, warrior):
    def __init__(self):
        super(type, self).__init__(self, warrior_weapon, mage_weapon)
        type = input("Would you like to be a warrior or mage?")
        if type == "warrior":
            warrior_weapon.lower() == "knife"
            warrior.warrior_skills.lower() == ["stab", "knife throw", "punch"]
            user("bla", "bla", "bla") == warrior("bla", "bla", "bla")
        if type == "mage":
            mage_weapon.lower() == "staff"
            mage.mage_skills.lower() == ["fireball", "lazarbeam", "heal", "punch"]
            user("bla", "bla", "bla") == mage("bla", "bla", "bla")
    #this is a substitute for josephine's code
#HOW DO I MAKE THIS WORKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
#the problem is that warrior_weapon is in init
class stuff_you_can_do():
    def start_fight():
        x = input("Would you like to attack/buff, give up, or equip/unequip?")
        if x.lower() == "attack/buff":
            stuff_you_can_do.attack_or_buff()
        if x.lower() == "give up":
            stuff_you_can_do.give_up()
        if x.lower() == "equip/unequip":
            stuff_you_can_do.equip_or_unequip()
            
    def attack_or_buff():
        #type is part of josephine's code
        if type == "warrior" and warrior.weapon.lower() == "knife":
            x = input("Would you like to use stab, knife throw, equip/unequip, or give up?(Buff not available for warriors.)")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()
        elif type == "mage" and mage.weapon.lower() == "staff":
            x = input("Would you like to use fireball, lazarbeam, punch, heal, equip/unequip, or give up?")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()
        elif type == "warrior" and warrior.weapon.lower() == "fist":
            x = input("Would you like to use punch, give up, or equip/unequip?")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()
        elif type == "mage" and mage.weapon.lower() == "fist":
            x = input("Would you like to use punch, give up, or equip/unequip?")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()

    def give_up():
        x = input("Are you sure?: Yes or No")
        if x.lower() == "yes":
            print("You lose.")
        if x.lower() == "no":
            x = input("Would you like to attack/buff, give up, or equip/unequip?")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()

    def equip_or_unequip():
        x = input("Would you like to equip or unequip?")
        if x.lower() == "equip":
            warrior.weapon.lower() == "knife"
            mage.weapon.lower() == "staff"
        if x.lower() == "unequip":
            warrior.weapon.lower() == "fist"
            mage.weapon.lower() == "fist"

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def __init__(self, start_fight, attack_or_buff, give_up, equip_or_unequip):
        self.start_fight = start_fight
        self.attack_or_buff = attack_or_buff
        self.give_up = give_up
        self.equip_or_unequip = equip_or_unequip

        if self.start_fight.lower() == "start fight" and self.give_up.lower() == "no" and self.attack_or_buff.lower() == "yes":
            if user.types.lower() == "warrior":
                y = input("Would you like to use stab, knife throw, punch, equip/unequip, or give up?(Buff not available for warriors.)")
            elif user.types.lower() == "mage":
                y = input("Would you like to use fireball, punch, heal, equip/unequip, or give up?")
        elif self.attack_or_buff.lower() == "no":
            input("Would you like to attack/buff, give up, or equip/unequip?")
        
            #not sure if user == warrior/mage works
        elif self.start_fight.lower() == "no":
            input("Would you like to start the fight, give up, or equip/unequip?")
            self.attack_or_buff.lower() == "no"
        
        elif self.give_up.lower() == "give up" and self.start_fight.lower() == "no":
            x = input("Are you sure?")
            if x.lower() == "yes": 
                print("You lose.")
            elif x.lower() == "no":
                input("Would you like to start the fight, give up, or equip/unequip?")

        elif self.give_up.lower() == "no":
            input("Would you like to start the fight, give up, or equip/unequip?")
        
        elif self.equip_or_unequip().lower() == "equip" and user.types.lower() == "warrior":
            y = input("Would you like to use stab, knife throw, punch, equip/unequip, or give up?(Buff not available for warriors.)")
        elif self.equip_or_unequip().lower() == "unequip" and user.types.lower() == "warrior":
            y = input("Would you like to use equip/unequip, punch, or give up?")
        elif self.equip_or_unequip().lower() == "equip" and user.types.lower() == "mage":
            y = input("Would you like to use fireball, punch, heal, equip/unequip, or give up?")
        elif self.equip_or_unequip().lower() == "unequip" and user.types.lower() == "mage":
            y = input("Would you like to use equip/unequip, punch, or give up?")
 
         

    
    
    

    
stuff_you_can_do.give_up()
    #fill in stuff_you_can_do()
    


    

    


        
#start_fight = "P"
#attack/buff = "F"
#give_up = "L"
#equip/unequip = "E"


