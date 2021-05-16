# This is an inventory system
# Also prices aren't final
import typey


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


class Weapon(item):
    def get_attack(self):
        return self.attack

    def damage(self, deal):
        return self.attack - deal


class Armor(item):
    def get_defense(self):
        return self.defense


class Potion(item):
    def get_heal(self):
        return self.heal_level


class inventory():
    def __init__(self, placeholder):
        self.placeholder = placeholder


def test_weapon():
    weapon = Weapon("Sword", 12, 0, 0, 21, 32)
    typey.typingprint(str(weapon.get_name()))
    typey.typingprint(str(weapon.get_attack()))
    y = 50
    typey.typingprint(str(y))
    y = y - weapon.get_attack()
    typey.typingprint(str(y))


def test_armor():
    armor = Armor("Iron Armor", 0, 13, 0, 21, 27)
    typey.typingprint(str(armor.get_name()))
    typey.typingprint(str(armor.get_defense()))


def test_potion():
    # I havn't decided on a price for it yet.
    potion = Potion("nea_potion", 0, 0, 21, 2, 500)
    typey.typingprint(str(potion.get_name()))
    typey.typingprint(str(potion.get_heal()))
