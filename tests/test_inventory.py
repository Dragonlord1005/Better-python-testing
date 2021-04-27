# This is an inventory system


class item():
    # Initiates
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight



