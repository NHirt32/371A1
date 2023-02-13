# Represents the information in the cell of the table in memory
class Cell:
    def __init__(self, items):
        self.items = items
        self.value = 0
        self.weight = 0
        if len(items) > 0:
            for item in self.items:
                self.value = self.value + item.price

        if len(items) > 0:
            for item in self.items:
                self.weight = self.weight + item.weight