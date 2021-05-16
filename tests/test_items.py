# This is an inventory system
# Also prices aren't final
import typey


class item():
    '''Defines item class which is used for a lot of things'''
    def __init__(self, name, attack, defense, heal_level, weight, price):
        '''Initializes and gathers all the info needed for an item'''
        self.name = name
        self.weight = weight
        self.price = price
        self.attack = attack
        self.defense = defense
        self.heal_level = heal_level

    def get_name(self):
        '''Get the name of an item'''
        return self.name

    def get_weight(self):
        '''Get the weight of an item'''
        return self.weight

    def get_price(self):
        '''Get the price of an item'''
        return self.price


class Weapon(item):
    '''Defines Weopon class'''
    def get_attack(self):
        '''Gets the level of attack for the weopon'''
        return self.attack

    def damage(self, deal):
        '''Deals damage'''
        return self.attack - deal


class Armor(item):
    '''Defines armor class'''
    def get_defense(self):
        '''Gets the defense value'''
        return self.defense


class Potion(item):
    '''Defines potion class'''
    def get_heal(self):
        '''Gets the heal level'''
        return self.heal_level


class Inventory():
    '''Defines inventory class'''
    def __init__(self, placeholder):
        self.placeholder = placeholder


def test_weapon():
    '''Initiates the testing powers for weopons'''
    weapon = Weapon("Sword", 12, 0, 0, 21, 32)
    typey.typingprint(str(weapon.get_name()))
    typey.typingprint(str(weapon.get_attack()))
    y = 50
    typey.typingprint(str(y))
    y = y - weapon.get_attack()
    typey.typingprint(str(y))


def test_armor():
    '''Initiates the testing powers for armors'''
    armor = Armor("Iron Armor", 0, 13, 0, 21, 27)
    typey.typingprint(str(armor.get_name()))
    typey.typingprint(str(armor.get_defense()))


def test_potion():
    '''
    Activates the awesomeness of test_potion
    I havn't decided on a price for it yet.
    '''
    potion = Potion("nea_potion", 0, 0, 21, 2, 500)
    typey.typingprint(str(potion.get_name()))
    typey.typingprint(str(potion.get_heal()))
