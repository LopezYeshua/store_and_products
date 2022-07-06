class Store:
    def __init__(self, name, products = []):
        self.name = name
        self.products = products

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        self.products.pop(id)

    def inflation(self, percent_increase):
        for i in range(0,len(self.products)):
            self.products[i].price += self.products[i].price * percent_increase
        return self

    def set_clearance(self, category, percent_discount):
        pass
