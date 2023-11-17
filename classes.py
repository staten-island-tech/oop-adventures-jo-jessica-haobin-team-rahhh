

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






