# This is an inventory system and uses classes
# Every item has a name, weight, and price

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

# Now we need a weapon that also has damamge in addition to defense
# We'll use inheritance to do this
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

# Now we need armour that also has defense in addition to weight
# We'll use inheritance to do this
class Armor(Item):
    """Defines armor class"""

    def __init__(self, name, defense, weight, price):
        """Initializes everything for this class"""
        super().__init__(name, weight, price)
        self.defense = defense

    def get_defense(self):
        """Gets the defense value"""
        return self.defense

# Now we need an inventory system that hooks into all of this
# We'll use classes
class Inventory:
    """Defines inventory class"""

    def __init__(self):
        """Initializes the inventory"""
        self.inventory = []

    def add_item(self, item):
        """Adds an item to the inventory"""
        self.inventory.append(item)

    def remove_item(self, item):
        """Removes an item from the inventory"""
        self.inventory.remove(item)

    def get_inventory(self):
        """Gets the inventory"""
        return self.inventory

    def get_total_weight(self):
        """Gets the total weight of the inventory"""
        total_weight = 0
        for item in self.inventory:
            total_weight += item.get_weight()
        return total_weight

    def get_total_price(self):
        """Gets the total price of the inventory"""
        total_price = 0
        for item in self.inventory:
            total_price += item.get_price()
        return total_price

    def get_total_attack(self):
        """Gets the total attack of the inventory"""
        total_attack = 0
        for item in self.inventory:
            if isinstance(item, Weapon):
                total_attack += item.get_attack()
        return total_attack

    def get_total_defense(self):
        """Gets the total defense of the inventory"""
        total_defense = 0
        for item in self.inventory:
            if isinstance(item, Armor):
                total_defense += item.get_defense()
        return total_defense

# Now we need tests for weapons that uses pytest
# We'll use def
def test_weapon():
    """Tests weapon class"""
    weapon = Weapon("Sword", 10, 2, 10)
    assert weapon.get_name() == "Sword"
    assert weapon.get_weight() == 2
    assert weapon.get_price() == 10
    assert weapon.get_attack() == 10
    
# Now we need tests for armor that uses pytest
# We'll use def
def test_armor():
    """Tests armor class"""
    armor = Armor("Iron Armor", 10, 2, 10)
    assert armor.get_name() == "Iron Armor"
    assert armor.get_weight() == 2
    assert armor.get_price() == 10
    assert armor.get_defense() == 10
# Now we need tests for inventory that uses pytest
# We'll use def
def test_inventory():
    """Tests inventory class"""
    inventory = Inventory()
    assert inventory.get_inventory() == []
    assert inventory.get_total_weight() == 0
    assert inventory.get_total_price() == 0
    assert inventory.get_total_attack() == 0
    assert inventory.get_total_defense() == 0
    weapon = Weapon("Sword", 10, 2, 10)
    armor = Armor("Iron Armor", 10, 2, 10)
    inventory.add_item(weapon)
    inventory.add_item(armor)
    assert inventory.get_inventory() == [weapon, armor]
    assert inventory.get_total_weight() == 4
    assert inventory.get_total_price() == 20
    assert inventory.get_total_attack() == 10
    assert inventory.get_total_defense() == 10
    inventory.remove_item(weapon)
    assert inventory.get_inventory() == [armor]
    assert inventory.get_total_weight() == 2
    assert inventory.get_total_price() == 10
    assert inventory.get_total_attack() == 0
    assert inventory.get_total_defense() == 10
