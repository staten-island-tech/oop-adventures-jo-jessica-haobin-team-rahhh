class user():
    def __init__(self, name:str, health:int, types:str, weapon:str, skills:str):
        self.name = name
        self.health = health
        self.types =  types
        self.weapon = weapon
        self.skills = skills
        #health = 100


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

    def equip_or_unequip():
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



    
    
    
    
   


        
#start_fight = "P"
#attack/buff = "F"
#give_up = "L"
#equip/unequip = "E"
    def __init__(self, name, health):
        self.name = name
        self.health = health
        #health = 100 
    def __str__(self) :
        return f"{self.name}, {self.health}"

class warrior(user):
    def __init__(self, name, health, stab, knife_throw):
        super().__init__(name, health)
        self.stab = stab
        self.knife_throw = knife_throw
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.stab}, {self.knife_throw}"

class mage(user):
    def __init__(self, name, health, fireball, heal):
        super().__init__(name, health)
        self.fireball = fireball
        self.heal = heal
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.fireball}, {self.heal}"
    
class enemy(user):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage 
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.damage}"
