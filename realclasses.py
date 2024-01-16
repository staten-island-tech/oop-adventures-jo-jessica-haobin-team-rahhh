class user():
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

class stuff_you_can_do(): 
    def attacks(self, attack, heal, start_fight):
        self.start_fight = start_fight
        start_fight = "P"
        self.attack = attack
        attack = "F"
        self.heal = heal
        heal = "H"


#code doesn't work