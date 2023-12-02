class Merchant:
    def __init__(self, name, products, coins):
        self.name = name
        self.products = products
        self.coins = coins
    def sell(self, item, amount):
        self.products.remove(item)
        print(f"You have purchased {item}!")
        self.coins.append(amount)
        return item
    def buy(self, item, amount):
        self.products.append(item)
        self.coins.remove(amount)
        print(f"You have sold {item}!")

        