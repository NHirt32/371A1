
class item:
    """Represents a knapsack item."""
    def __init__(self, ID, weight, price):
        self.ID = int(ID)
        self.weight = int(weight)
        self.price = int(price)


    def get_ID(self):
        """Returns a knapsack item's ID."""
        return self.ID

    def get_weight(self):
        """Returns a knapsack item's weight."""
        return self.weight

    def get_price(self):
        """Returns a knapsack item's price."""
        return self.price