# This is an inventory system
import test_type as typer

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

    def damage(self, deal):
        return self.attack - deal


yep = weapon("Sword", 12, 12, 53)
print(yep.get_name())
print(yep.get_attack())
y = 50
print(y)
y = y - yep.get_attack()
typer.typingprint(str(y))
