class Customer:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []
        
    def get_order_count(self):
        return len(self.orders)
        
    def get_total(self):
        total = 0
        for order in self.orders:
            total += order.get_total()
        return total
        
    def add_order(self, order):
        self.orders.append(order)
        
    def display_summary(self):
        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${0:.2f}".format(self.get_total()))
        
    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}\n".format(self.name))
        for order in self.orders:
            order.display_receipt()
            print()