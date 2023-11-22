class user():
    def character(self, name, health):
        self.name = name
        self.health = health
        #health = 100

class warrior(user):
    def __init__(self, name, health, warrior_skills):
        super().__init__(name, health)
        self.warrior_skills = warrior_skills
    def __str__(self) :
        return f"{self.name}, {self.health}, {self.warrior_skills}"

class mage(user):
    def __init__(self, name, health, mage_skills):
        super().__init__(name, health)
        self.mage_skills = mage_skills
    def __str__(self):
        return f"{self.name}, {self.health}, {self.mage_skills}"

class stuff_you_can_do(): 
    def attacks(self, attack, heal, start_fight):
        self.start_fight = start_fight
        start_fight = "P"
        self.attack = attack
        attack = "F"
        self.heal = heal
        heal = "H"

warrior("Jess", 100, "Berserker", "[Stab, Throw Knife]")
#code doesn't work