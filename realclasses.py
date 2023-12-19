class user():
    def __init__(self, name:str, health:int, types:str, weapon:str, skills:str):
        self.name = name
        self.health = health
        self.types =  types
        self.weapon = weapon
        self.skills = skills
        #health = 100
#this is a substitute for josephine's code

weapon = "fist"

class stuff_you_can_do():
    def start_fight():
        x = input("Would you like to give up or equip/unequip?")
        if x.lower() == "give up":
            stuff_you_can_do.give_up()
        if x.lower() == "equip/unequip":
            stuff_you_can_do.equip_or_unequip()
    
    def give_up():
        x = input("Are you sure?: Yes or No")
        if x.lower() == "yes":
            print("You lose.")
        if x.lower() == "no":
            x = input("Would you like to give up or equip/unequip?")
            if x.lower() == "equip/unequip":
                stuff_you_can_do.equip_or_unequip()
            if x.lower() == "give up":
                stuff_you_can_do.give_up()

    def equip_or_unequip(user):
        
        x = input("Would you like to equip or unequip?")
        if x.lower() == "equip":
            y = input("Would you like to use the knife or the staff?")
            if y.lower() == "knife":
                weapon == "knife"
            if y.lower() == "staff":
                weapon == "staff"
        if x.lower() == "unequip":
            weapon == "fist"
        z = input("Would you like to give up or equip/unequip?")
        if z.lower() == "equip/unequip":
            stuff_you_can_do.equip_or_unequip()
        if z.lower() == "give up":
            stuff_you_can_do.give_up()



    
    
    
    
    
stuff_you_can_do.start_fight()
    
    
    
   


        
#start_fight = "P"
#attack/buff = "F"
#give_up = "L"
#equip/unequip = "E"


