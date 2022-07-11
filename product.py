class Product:
    all_products = []

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        Product.all_products.append(self)

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change

    def print_info(self):
        print(self.name)
        print(self.category)
        print(self.price)