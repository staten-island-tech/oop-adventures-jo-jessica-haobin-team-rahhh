class user():
    def __init__(self, name:str, health:int, types:str, weapon:str, skills:str):
        self.name = name
        self.health = health
        self.types =  types
        self.weapon = weapon
        self.skills = skills
        #health = 100
#this is a substitute for josephine's code

class stuff_you_can_do(user):
    def start_fight(self):
        x = input("Would you like to attack/buff, give up, or equip/unequip?")
        if x.lower() == "attack/buff":
            stuff_you_can_do.attack_or_buff()
        if x.lower() == "give up":
            stuff_you_can_do.give_up()
        if x.lower() == "equip/unequip":
            stuff_you_can_do.equip_or_unequip()
    
    def give_up(self):
        x = input("Are you sure?: Yes or No")
        if x.lower() == "yes":
            print("You lose.")
        if x.lower() == "no":
            x = input("Would you like to attack/buff, give up, or equip/unequip?")
            if x.lower() == "attack/buff":
                stuff_you_can_do.attack_or_buff()
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()


    def attack_or_buff():
        if weapon.lower == "knife":
            x = input("Would you like to use stab, knife throw, equip/unequip, or give up?(Buff not available for warriors.)")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()
        elif weapon.lower == "staff":
            x = input("Would you like to use fireball, lazarbeam, punch, heal, equip/unequip, or give up?")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()
        elif weapon.lower == "fist":
            x = input("Would you like to use punch, give up, or equip/unequip?")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()

        def equip_or_unequip():
            x = input("Would you like to equip or unequip?")
            if x.lower() == "equip":
                y = input("Would you like to use the knife or the staff?")
                if y.lower() == "knife":
                    weapon.lower() == "knife"
                if y.lower() == "staff":
                    weapon.lower() == "knife"
            if x.lower() == "unequip":
                weapon.lower() == "fist"

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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


