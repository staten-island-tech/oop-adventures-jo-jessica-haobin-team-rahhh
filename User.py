class User:
    def __init__(self, name, currency, inventory, power):
        self.name = name
        self.currency = currency
        self.inventory = inventory
        self.power = power
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    def remove_currency(self, coins):
        self.currency -= coins
        print(f"COINS : {self.currency}")
    def sell(self, item):
        

        