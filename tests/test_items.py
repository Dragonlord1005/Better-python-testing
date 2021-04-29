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


class armor(item):
    def __init__(self, name, armor, weight, price):
        self.name = name
        self.armor = armor
        self.weight = weight
        self.price = price

    def get_armor(self):
        return self.armor


def test_weapon():
    yep = weapon("Sword", 12, 12, 53)
    print(yep.get_name())
    print(yep.get_attack())
    y = 50
    typer.typingprint(str(y))
    y = y - yep.get_attack()
    typer.typingprint(str(y))


def test_armor():
    hi = armor("Iron Armor", 13, 31, 78)
    print(hi.get_name())
    print(hi.get_armor())
