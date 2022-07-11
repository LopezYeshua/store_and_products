class Store:
    def __init__(self, name, products = []):
        self.name = name
        self.products = products

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        self.products.pop(id)

    def inflation(self, percent_increase):
        for product in self.products:
            self.products[product].update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        self.products[category].update_price(percent_discount, False)