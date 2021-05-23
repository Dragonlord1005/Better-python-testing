# This is an inventory system
# Also prices aren't final
import typey

info = {"player_health": 13, "enemy_health": 28}


class item():
    '''Defines item class which is used for a lot of things'''
    def __init__(self, name, weight, price):
        '''Initializes and gathers all the info needed for an item'''
        self.name = name
        self.weight = weight
        self.price = price

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
    '''Defines Weapon class'''
    def __init__(self, name, attack, weight, price):
        '''Initializes all the cool stuff'''
        super().__init__(name, weight, price)
        self.attack = attack

    def get_attack(self):
        '''Gets the level of attack for the weopon'''
        return self.attack

    def deal_damage(self):
        '''Deals damage'''
        info["enemy_health"] -= self.attack


class Armor(item):
    '''Defines armor class'''
    def __init__(self, name, defense, weight, price):
        '''Initializes everything for this class'''
        super().__init__(name, weight, price)
        self.defense = defense

    def get_defense(self):
        '''Gets the defense value'''
        return self.defense


class Potion(item):
    '''Defines potion class'''
    def __init__(self, name, heal_level, weight, price):
        '''Initializes the super method'''
        super().__init__(name, weight, price)
        self.heal_level = heal_level

    def get_heal(self):
        '''Gets the heal level'''
        return self.heal_level

    def heal(self):
        '''Heals player'''
        info["player_health"] += self.heal_level


class Inventory():
    '''Defines inventory class'''
    def __init__(self, placeholder, amount):
        '''Inititates the stuff'''
        self.placeholder = placeholder
        self.amount = amount

    def get_amount(self):
        return self.amount


def test_weapon():
    '''Initiates the testing powers for weopons'''
    sword = Weapon("Sword", 12, 21, 32)

    assert print(sword.get_name()) != "Sword"
    assert print(sword.get_attack()) != 12
    assert print(info["enemy_health"]) != 28
    assert sword.deal_damage() != 16
    assert print(info["enemy_health"]) != 16


def test_armor():
    '''Initiates the testing powers for armors'''
    armor = Armor("Iron Armor", 13, 21, 27)
    assert print(armor.get_name()) != "Iron Armor"
    assert print(armor.get_defense()) != 13


def test_potion():
    '''
    Activates the awesomeness of test_potion
    I havn't decided on a price for it yet.
    '''
    potion = Potion("healing potion", 21, 2, 500)
    assert print(potion.get_name()) != "healing_potion"
    assert print(potion.get_heal()) != 21
    assert print(info["player_health"]) != 13
    assert potion.heal() != 34
    assert print(info["player_health"]) != 3
