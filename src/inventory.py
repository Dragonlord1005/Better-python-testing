# This is an inventory system and uses classes
# Every item has a name, weight, and price


class Item: # Item class
    """Defines item class which is used for a lot of things"""

    def __init__(self, name, weight, price):
        """Initializes and gathers all the info needed for an item"""
        self.name = name # Name of the item
        self.weight = weight # Weight of the item
        self.price = price # Price of the item

    def get_name(self):
        """Get the name of an item"""
        return self.name # Returns the name of the item

    def get_weight(self):
        """Get the weight of an item"""
        return self.weight # Returns the weight of the item
 
    def get_price(self):
        """Get the price of an item"""
        return self.price # Returns the price of the item
 

# Now we need a weapon that also has damamge in addition to defense
# We'll use inheritance to do this
class Weapon(Item):
    """Defines Weapon class"""

    def __init__(self, name, attack, weight, price): 
        """Initializes all the cool stuff"""
        super().__init__(name, weight, price) # Initializes the item class
        self.attack = attack # Sets the attack level

    def get_attack(self):
        """Gets the level of attack for the weopon"""
        return self.attack # Returns the attack level

    def deal_damage(self):
        """Deals damage"""
        info["enemy_health"] -= self.attack # Deals damage to the enemy


# Now we need armour that also has defense in addition to weight
# We'll use inheritance to do this
class Armor(Item): # Armor class
    """Defines armor class"""

    def __init__(self, name, defense, weight, price): 
        """Initializes everything for this class""" 
        super().__init__(name, weight, price) # Initializes the item class
        self.defense = defense # Sets the defense level

    def get_defense(self):
        """Gets the defense value"""
        return self.defense # Returns the defense level


# Now we need an inventory system that hooks into all of this
# We'll use classes
class Inventory: # Inventory class  
    """Defines inventory class"""

    def __init__(self): 
        """Initializes the inventory"""
        self.inventory = [] # Initializes the inventory list as an empty list

    def add_item(self, item):
        """Adds an item to the inventory"""
        self.inventory.append(item) # Adds the item to the inventory

    def remove_item(self, item):
        """Removes an item from the inventory"""
        self.inventory.remove(item) # Removes the item from the inventory

    def get_inventory(self):
        """Gets the inventory"""
        return self.inventory # Returns the inventory

    def get_total_weight(self):
        """Gets the total weight of the inventory"""
        total_weight = 0 # Initializes the total weight
        for item in self.inventory: # For each item in the inventory
            total_weight += item.get_weight() # Adds the weight of each item to the total weight
        return total_weight # Returns the total weight

    def get_total_price(self): # Gets the total price of the inventory
        """Gets the total price of the inventory"""
        total_price = 0 # Initializes the total price
        for item in self.inventory: # For each item in the inventory
            total_price += item.get_price() # Adds the price of each item to the total price
        return total_price # Returns the total price

    def get_total_attack(self): # Gets the total attack a weapon has in the inventory
        """Gets the total attack of a weapon in the inventory"""
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
