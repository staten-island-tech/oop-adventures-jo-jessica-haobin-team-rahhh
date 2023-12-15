class Merchant:
    def __init__(self, name, products):
        self.name = name
        self.products = products
<<<<<<< HEAD
        self.coins = coins
    def sell(self, item, amount):
        self.products.remove(item)
        print(f"You have purchased {item}!")
        self.coins.append(amount)
        return item
    def buy(self, item, amount):
        self.products.append(item)
        self.coins.remove(amount)
=======
    def sell(self, item):
        self.products.remove(item)
        print(f"You have purchased {item}!")
        return item
    def buy(self, item):
        self.products.append(item)
>>>>>>> b875963dbbf0afc230141ae46d4f715bafa16f16
        print(f"You have sold {item}!")
        return item
    

        