





class inventory:
    def __init__(self, inventory):
        self.inventory = inventory
    def pick_stuff_up(self, items):
        self.inventory.append(items)
        print(self.inventory)
    def throw_stuff_out(self, items):
        self.inventory.remove(items)
        print(self.inventory)
    inventory = ['thing 1', 'thing 2', 'thing 3', 'thing 4', 'thing 5', 'thing 6']
    pick_stuff_up(inventory, 'thing 7')




    
