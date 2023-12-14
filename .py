import json

class enemy():
    def __init__(self, name, health, type, damage):
        self.name = name
        self.health = health
        self.type = type
        self.damage = damage
        
    def __str__(self):
        return f"{self.name}, {self.health}, {self.type}, {self.damage}"
    


with open('something.json', mode='r') as infile:
    data = json.load(infile)

def enemy2():
    a = input('Monster name: ')
    b = int(input('Monster health'))
    c = input('Monster type')
    d = int(input('Monster damage'))

    monster = enemy(a, b, c, d)

    data.append(
        {
            "Name": monster.name,
            "Health": monster.health,
            "Type": monster.type,
            "Damage": monster.damage
        }
    )

    