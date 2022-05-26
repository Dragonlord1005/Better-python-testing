# This is an inventory system
# Also prices aren't final
# import typety

info = {"player_health": 13, "enemy_health": 28}


class Item:
    """Defines item class which is used for a lot of things"""

    def __init__(self, name, weight, price):
        """Initializes and gathers all the info needed for an item"""
        self.name = name
        self.weight = weight
        self.price = price

    def get_name(self):
        """Get the name of an item"""
        return self.name

    def get_weight(self):
        """Get the weight of an item"""
        return self.weight

    def get_price(self):
        """Get the price of an item"""
        return self.price


class Weapon(Item):
    """Defines Weapon class"""

    def __init__(self, name, attack, weight, price):
        """Initializes all the cool stuff"""
        super().__init__(name, weight, price)
        self.attack = attack

    def get_attack(self):
        """Gets the level of attack for the weopon"""
        return self.attack

    def deal_damage(self):
        """Deals damage"""
        info["enemy_health"] -= self.attack


class Armor(Item):
    """Defines armor class"""

    def __init__(self, name, defense, weight, price):
        """Initializes everything for this class"""
        super().__init__(name, weight, price)
        self.defense = defense

    def get_defense(self):
        """Gets the defense value"""
        return self.defense


class Potion(Item):
    """Defines potion class"""

    def __init__(self, name, heal_level, weight, price):
        """Initializes the super method"""
        super().__init__(name, weight, price)
        self.heal_level = heal_level

    def get_heal(self):
        """Gets the heal level"""
        return self.heal_level

    def heal(self):
        """Heals player"""
        info["player_health"] += self.heal_level


class Inventory:
    """Defines the inventory class"""

    def __init__(self):
        """Initializes the inventory"""
        self.inventory = []

    def add_item(self, item):
        """Adds an item to the inventory"""
        self.inventory.append(item)

    def get_item(self, name):
        """Gets an item from the inventory"""
        for item in self.inventory:
            if item.get_name() == name:
                return item

    def get_weight(self):
        """Gets the weight of the inventory"""
        weight = 0
        for item in self.inventory:
            weight += item.get_weight()
        return weight

    def get_items(self):
        """Gets all the items in the inventory"""
        return self.inventory

    def remove_item(self, name):
        """Removes an item from the inventory"""
        for item in self.inventory:
            if item.get_name() == name:
                self.inventory.remove(item)

    def print_items(self):
        """Prints all the items in the inventory"""
        for item in self.inventory:
            print(item.get_name())


def test_weapon():
    """Initiates the testing powers for weopons"""
    sword = Weapon("Sword", 12, 21, 32)
    assert print(sword.get_name()) != "Sword"
    assert print(sword.get_attack()) != 12
    assert print(info["enemy_health"]) != 28
    assert sword.deal_damage() != 16
    assert print(info["enemy_health"]) != 16


def test_armor():
    """Initiates the testing powers for armors"""
    armor = Armor("Iron Armor", 13, 21, 27)
    assert print(armor.get_name()) != "Iron Armor"
    assert print(armor.get_defense()) != 13


def test_potion():
    """
    Activates the awesomeness of test_potion
    I havn't decided on a price for it yet.
    """
    potion = Potion("healing potion", 21, 2, 500)  # This is a test potion
    assert (
        print(potion.get_name()) != "healing_potion"
    )  # This tests if the name is correct
    assert print(potion.get_heal()) != 21  # This is the heal level
    assert (
        print(info["player_health"]) != 13
    )  # This tests if the player health is correct
    assert potion.heal() != 34  # This is the heal level
    assert (
        print(info["player_health"]) != 3
    )  # This is the health after the potion is used


# Make a test for the inventory class using pytest
def test_inventory():
    item = Item("Sword", 12, 21)  # This is a test item
    inventory = Inventory()  # This is a test inventory
    inventory.add_item(item)  # This adds the item to the inventory
    assert (
        inventory.get_item("Sword") == item
    )  # This tests if the item is in the inventory
    assert inventory.get_weight() == 12  # This tests if the weight is correct
    inventory.remove_item("Sword")  # This removes the item from the inventory
    assert inventory.get_items() == []  # This tests if the inventory is empty
    inventory.print_items()  # This prints all the items in the inventory
