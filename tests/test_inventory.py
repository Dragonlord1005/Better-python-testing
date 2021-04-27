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

    def get_price(self):
        return self.price


class weapon(item):
    def __init__(self, name, attack, weight, price):
        self.name = name
        self.attack = attack
        self.weight = weight
        self.price = price

    def get_attack(self):
        return self.attack
    def damage(self, input):
      return self.attack - input


yep = weapon("Sword", 23, 21, 53)
print(yep.get_name())
print(yep.damage(10))

