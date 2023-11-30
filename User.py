class User:
    def __init__(self, name, hp, currency, inventory, type):
        self.name = name
        self.HP = hp
        self.currency = currency
        self.inventory = inventory
        self.type = type
    def buy(self, item):
        self.inventory.append(item)
        print(f"INVENTORY : {self.inventory}")
    def remove_currency(self, coins):
        self.currency -= coins
        print(f"COINS : {self.currency}")
    def sell(self, item):
        self.inventory.remove(item)
        print(f"INVENTORY : {self.inventory}")
    def add_currency(self, coins):
        self.currency += coins
        print(f"COINS : {self.currency}")
    def GET_ATTACKED(self, dmg):
        self.HP -= dmg
        print(f"HP : {self.HP}")

class MAGE(User):
    def __init__(self, name, hp, currency, inventory, type, attack):
        super().__init__(name, hp, currency, inventory, type)
        self.attack = attack
        