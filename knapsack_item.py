
class item:
    def __init__(self, ID, weight, price):
        self.ID = int(ID)
        self.weight = int(weight)
        self.price = int(price)

    def get_ID(self):
        return self.ID

    def get_weight(self):
        return self.weight

    def get_price(self):
        return self.price