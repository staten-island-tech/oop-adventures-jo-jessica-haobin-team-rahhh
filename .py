import json

class enemy():
    def __init__(self, name, health, type, damage):
        self.name = name
        self.health = health
        self.type = type
        self.damage = damage
        
    def __str__(self):
        return f"{self.title}, {self.status}"
    


with open('data.json', mode='r') as infile:
     data = json.load(infile)

def enemy2():
     global monster
     a = input('Name: ')
     b = int(input('Health: '))
     c = input('Type: ')
     d = int(input('Damage: '))
     
     monster = enemy(a, b, c)
     
     data.append(
            {
               'name': monster.name,
               'health': monster.health,
               'type': monster.type
               'damage': monster.damage
            }
     ) 
          
     with open('data.json', mode='w') as outfile:
          json.dump(data, outfile, indent=4)



enemy2()