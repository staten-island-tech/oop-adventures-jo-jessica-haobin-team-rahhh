import json

class enemy():
    def __init__(self, name, health, damage, exp):
        self.name = name
        self.health = health
        self.damage = damage
        self.exp = exp
        
    def __str__(self):
        return f"{self.name}, {self.health}, {self.damage}, {self.exp}"
    


with open('something.json', mode='r') as infile:
    data = json.load(infile)

def enemy2():
    global data
    a = input('Monster name: ')
    b = int(input('Monster health: '))
    c = int(input('Monster damage: '))
    d = int(input('Monster exp: '))

    monster = enemy(a, b, c, d)

    data.append(
        {
            "Name": monster.name,
            "Health": monster.health,
            "Damage": monster.damage,
            "Exp": monster.exp
        }
    )

    with open('something.json', mode='w') as outfile:
        data = json.dump(data, outfile, indent=4)
    
enemy2()