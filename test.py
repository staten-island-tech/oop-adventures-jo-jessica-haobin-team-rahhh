class User:
    def __init__(self, name, hp, currency, inventory, type, exp):
        self.name = name
        self.HP = hp
        self.currency = currency
        self.inventory = inventory
        self.type = type
        self.exp = exp
    def attack(self,enemy):
        enemy.hp = enemy.hp - 25
class ENEMY:
    def __init__(self, name,  hp):
        self.name = name
        self.hp = hp
Audrey = User("Audrey", 100, 50, [], 'water', 500)
Hao = ENEMY("Hao", 50)
Audrey.attack(Hao)
print(Hao.hp)