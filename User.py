class User:
    def __init__(self, name, coins, inventory, power):
        self.name = name
        self.coins = coins
        self.inventory = inventory
        self.power = power
    def buy(self, item, coins):
        self.inventory.append(item)
        self.coins.remove(coins)
        print(self.inventory)
        print(self.coins)