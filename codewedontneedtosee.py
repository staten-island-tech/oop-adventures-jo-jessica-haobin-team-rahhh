import json

class enemy():
    def __init__(self, name, health, damage, exp):
        self.name = name
        self.health = health
        self.damage = damage
        self.exp = exp
        
    def __str__(self):
        return f"{self.name}, {self.health}, {self.damage}, {self.exp}"
    


with open('data.json', mode='r') as infile:
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

    with open('data.json', mode='w') as outfile:
        data = json.dump(data, outfile, indent=4)

with open('items.json', mode='r') as  readfile:
    items = json.load(readfile)

def itemstuff():
    global items
    itemname = input('Name: ')
    ratebuff = float(input('Rate of Buff: '))
    partthatgetsbuffed = input('Part that gets buffed: ')

    items.append(
        {
            "Name": itemname,
            "Rate of Buff": ratebuff,
            "Part that get Buff": partthatgetsbuffed 
        }
    )

    with open('items.json', mode = 'w') as writefile:
        items = json.dump(items, writefile, indent=4)

itemstuff()
    
def answer_response(Options: list):
    Choices = input(f"{'/'.join(Options)}: ").lower()
    while Choices not in Options:
        Choices = input(f"{'/'.join(Options)}: ").lower()
    else:
        return
    