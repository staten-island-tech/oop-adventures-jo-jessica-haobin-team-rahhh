class Merchant:
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(f"You have purchased {item}!")
        return item
    def buy(self, item):
        self.products.append(item)
        print(f"You have sold {item}!")

        