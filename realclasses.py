class user():
    def __init__(self, name:str, health:int, types:str):
        self.name = name
        self.health = health
        self.types =  types
        #health = 100

class enemy(user):
    def __init__(self, name:str, health:int, types:str, damage:int):
        super().__init__(name, health, types)
        self.damage = damage
    def __str__(self):
        return f"{self.name}, {self.health}, {self.types}, {self.damage}"


class warrior(user):
    def __init__(self, name:str, health:int, types:str, warrior_skills:str):
        super().__init__(name, health, types)
        self.warrior_skills = warrior_skills
        print("Name:",name,"Health:",health, "Types:" ,types, "Skills:" ,warrior_skills,)
        #warrior_skills(with weapon equipped) are stab and throw knife
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.types}, {self.warrior_skills}"

class mage(user):
    def __init__(self, name, health, types, mage_skills):
        super().__init__(health, name, types)
        self.mage_skills = mage_skills
        print("Name:" ,name, "Health:" ,health, "Types:" ,types, "Skills:" ,mage_skills,)
        #mage_skills(with weapon equipped) are fireball and heal
    def __str__(self):
        return f"{self.name}, {self.health}, {self.types}, {self.mage_skills}"

class stuff_you_can_do(warrior):
    global unequip
    def start_fight():
        # x = input(what would you like to do?) -> main
        if x == "P".lower():
            y = input("Would you like to attack or heal?") 
            def attack():
            #can only use if choose start_fight
                if y == "F".lower():
                    input("What attack would you like to do? Stab or throw knife?")
            def heal():
            #can only use if choose start_fight
                if y == "H".lower():
                    print("You have healed 20 health.")
    def give_up():
        if x == "L".lower():
            print("Game Over")

        







        
#start_fight = "P"
#attack = "F"
#heal = "H"
#give_up = "L"
#equip = "E"


warrior("Jess", 100, "Berserker", "[Stab, Throw Knife]")
#code doesn't work