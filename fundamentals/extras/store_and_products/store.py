class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products
    
    def add_product(self, new_product):
        self.products.append(new_product)
        self.products[-1].product_id = len(self.products)-1
        return self

    def sell_product(self, id):
        for product in self.products:
            if product.product_id == id:
                product = self.products.pop(product.product_id)
                print("Item Sold:")
                product.print_info()
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        print(f"{category} items are on {round((percent_discount*100))}% discount!!")
        return self