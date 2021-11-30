class Product:
    def __init__(self, name, price, category, product_id=0):
        self.name = name
        self.price = price
        self.category = category
        self.id = product_id
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change
        self.price = round(self.price, 2)
        return self

    def print_info(self):
        print(f"Product Name: {self.name}, Category: {self.category}, Price: {str(self.price)}, ID: {str(self.product_id)}")
        return self