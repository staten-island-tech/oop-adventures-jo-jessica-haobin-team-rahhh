class user():
    def character(self, name, health:int):
        self.name = name
        self.health = health
        #health = 100

class warrior(user):
    def __init__(self, name, health, warrior_skills):
        super().__init__(health)
        super().__init__(name)
        self.warrior_skills = warrior_skills
        #warrior_skills(with weapon equipped) are stab and throw knife
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.warrior_skills}"

class mage(user):
    def __init__(self, name, health, mage_skills):
        super().__init__(health)
        super().__init__(name)
        self.mage_skills = mage_skills
        #mage_skills(with weapon equipped) are fireball and heal
    def __str__(self):
        return f"{self.name}, {self.health}, {self.mage_skills}"

class stuff_you_can_do():
    global unequip
    def start_fight():
        # x = input(what would you like to do?) -> main
        if x == "P":
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
        if x == "L":
            print("Game Over")
    def attack():
        #can only use if choose start_fight
        if y == "F".lower():
            input("What attack would you like to do? Stab or throw knife?")
    def heal():
        #can only use if choose start_fight
        if y == "H".lower():
            print("You have healed 20 health.")
    def equip():
        if x = "E".lower():



        
#start_fight = "P"
#attack = "F"
#heal = "H"
#give_up = "L"
#equip = "E"


warrior("Jess", 100, "[Stab, Throw Knife]")
#code doesn't work