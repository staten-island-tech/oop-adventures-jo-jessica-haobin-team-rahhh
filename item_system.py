





class inventory:
    def __init__(self, inventory):
        self.inventory = inventory
    def pick_stuff_up(self, items):
        self.inventory.extend(items)
        print(self.inventory)
        return self.inventory
    def throw_stuff_out(self, items):
        self.inventory.remove(items)
        print(self.inventory)
        return self.inventory 
    




    
