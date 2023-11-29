class Merchant:
    def __init__(self, name, products, coins):
        self.name = name
        self.products = products
        self.coins = coins
    def sell(self, item, coins):
        self.products.remove(item)
        print(f"You have purchased {item}!")
        
        self.coins.append(coins)
        return item
    def buy(self, item, coins):
        self.products.append(item)
        self.coins.remove(coins)
        print(f"You have sold {item}!")

        