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

    def __init__(self, name, attack, weight, price, equipped):
        """Initializes all the cool stuff"""
        super().__init__(name, weight, price)
        self.attack = attack
        self.equipped = False

    def get_attack(self):
        """Gets the level of attack for the weopon"""
        return self.attack



# Now we need armour that also has defense in addition to weight
# We'll use inheritance to do this
class Armor(Item):
    """Defines armor class"""

    def __init__(self, name, defense, weight, price, equipped):
        """Initializes everything for this class"""
        super().__init__(name, weight, price)
        self.defense = defense
        self.equipped = False

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
        self.equipped_weapon = None
        self.equipped_armor = None

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

    def equip_weapon(self, weapon):
        """Equips a weapon"""
        self.equipped_weapon = weapon
        self.equipped_weapon.equipped = True

    def equip_armor(self, armor):
        """Equips an armor"""
        self.equipped_armor = armor
        self.equipped_armor.equipped = True

    def get_equipped_weapon(self):
        """Gets the equipped weapon"""
        return self.equipped_weapon

    def get_equipped_armor(self):
        """Gets the equipped armor"""
        return self.equipped_armor

    def unequip_weapon(self):
        """Unequips the weapon"""
        self.equipped_weapon.equipped = False
        self.equipped_weapon = None

    def unequip_armor(self):
        """Unequips the armor"""
        self.equipped_armor.equipped = False
        self.equipped_armor = None

    def get_equipped_attack(self):
        """Gets the attack value of the equipped weapon"""
        equipped_weapon = self.get_equipped_weapon()
        if equipped_weapon is None:
            return 0
        return equipped_weapon.get_attack()

    def get_equipped_defense(self):
        """Gets the defense value of the equipped armor"""
        equipped_armor = self.get_equipped_armor()
        if equipped_armor is None:
            return 0
        return equipped_armor.get_defense()
