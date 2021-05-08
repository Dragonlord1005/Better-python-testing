# This is an inventory system
# Also prices aren't final
import test_type as typer


class item():
    # Initiates
    def __init__(self, name, attack, defense, heal_level, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.attack = attack
        self.defense = defense
        self.heal_level = heal_level

    # Get name
    def get_name(self):
        return self.name

    # Get the weight
    def get_weight(self):
        return self.weight

    # Get the price
    def get_price(self):
        return self.price


class weapon(item):
    def get_attack(self):
        return self.attack

    def damage(self, deal):
        return self.attack - deal


class armor(item):
    def get_defense(self):
        return self.defense


class potion(item):
    def get_heal(self):
        return self.heal_level


def test_weapon():
    yep = weapon("Sword", 12, 0, 0, 21, 32)
    typer.typingprint(str(yep.get_name()))
    typer.typingprint(str(yep.get_attack()))
    y = 50
    typer.typingprint(str(y))
    y = y - yep.get_attack()
    typer.typingprint(str(y))


def test_armor():
    hi = armor("Iron Armor", 0, 13, 0, 21, 27)
    typer.typingprint(str(hi.get_name()))
    typer.typingprint(str(hi.get_defense()))


def test_potion():
    # The knights of NEA will find you
    # Also I havn't decided on a price for it yet so yeah.
    NEA = potion("nea_potion", 0, 0, 21, 2, 500)
    typer.typingprint(str(NEA.get_name()))
    typer.typingprint(str(NEA.get_heal()))
