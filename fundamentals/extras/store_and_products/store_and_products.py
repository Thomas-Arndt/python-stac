import store
import products

my_store = store.Store("The Pretty Cool Store")
my_store.add_product(products.Product("Deck of Cards", 4.99, "Game"))
my_store.add_product(products.Product("Scooter", 149.99, "Vehicle"))
my_store.add_product(products.Product("Red Paint", 9.99, "Paint"))

print("List of Products:")
for product in my_store.products:
    product.print_info()

my_store.inflation(0.05)

print("List of Products:")
for product in my_store.products:
    product.print_info()

my_store.set_clearance("Vehicle", 0.3)

print("List of Products:")
for product in my_store.products:
    product.print_info()

my_store.sell_product(1)

print("List of Products:")
for product in my_store.products:
    product.print_info()