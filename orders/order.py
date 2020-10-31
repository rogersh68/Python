class Order:
    def __init__(self):
        self.id = ""
        self.products = []
        
    def get_subtotal(self):
        sum = 0
        for product in self.products:
            sum += product.get_total_price()
        return sum
    
    def get_tax(self):
        return self.get_subtotal() * 0.065
    
    def get_total(self):
        return self.get_subtotal() + self.get_tax()
    
    def add_product(self, product):
        self.products.append(product)
        
    def display_receipt(self):
        print("Order: {}".format(self.id))
        for item in self.products:
            print("{} ({}) - ${:.2f}".format(item.name, item.quantity, item.get_total_price()))
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))