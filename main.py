from store import Store
from product import Product

prod1 = Product("Cucumbers", 35, "fruit")
prod2 = Product("Tomatos", 50, "fruit")
prod3 = Product("Potatoes", 100, "roots")
prod4 = Product("carrots", 1, "vegetables")
prod_list = [prod1, prod2, prod3, prod4]

grocery_store = Store("Amazon", prod_list)
new_product  = Product("beets", 20, "roots")
grocery_store.add_product(new_product)

print("g.p", grocery_store.products[0].name)
grocery_store.sell_product(2)
grocery_store.inflation(.2)
print(grocery_store.products[0].price)