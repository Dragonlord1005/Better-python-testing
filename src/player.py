# We will create a class for the player
# Gold, inventory, weapon damage, armor defense, will be in the inventory.py file

# First we need to import the classes we need from inventory.py
from inventory import Inventory, Item, Weapon, Armor

# The player will be able to choose their name at the beginning of the game, and it must be saved to a local file, along with other player information, such as gold, inventory, weapon damage, armor defense
# The player will have a starting gold of 300
# The player will have a starting inventory containing a stick that does 4 damage, and a leather amour piece that has a defense of 2
# The player information will be stored in playerdata.json in the json format and will be loaded when the game starts

# We must import the ability to read and write to json files
import json

class Player:
    """Defines the player class"""
    
        def __init__(self, name, gold, inventory):
            """Initializes the player class"""
            self.name = name # Sets the name
            self.gold = gold # Sets the gold
            self.inventory = inventory # Sets the inventory

        def get_name(self):
            """Gets the name"""
            return self.name

        def get_gold(self):
            """Gets the gold"""
            return self.gold

        def get_inventory(self):
            """Gets the inventory"""
            return self.inventory

        def add_gold(self, amount):
            """Adds gold to the player"""
            self.gold += amount

        def remove_gold(self, amount):
            """Removes gold from the player"""
            self.gold -= amount

        def load_player(self):
            """Loads the player data"""
            try:
                with open("playerdata.json", "r") as f:
                    player_data = json.load(f)
                    self.name = player_data["name"]
                    self.gold = player_data["gold"]
                    self.inventory = player_data["inventory"]
            except FileNotFoundError:
                # if it is not found then we will create a new file and prompt them for their name and fill out the rest of the information
                # The player will have a starting inventory containing a weapon stick that does 4 damage, and a leather amour piece that has a defense of 2
                with open("playerdata.json", "w") as f:
                    player_data = {}
                    player_data["name"] = input("What is your name? ")
                    player_data["gold"] = 300
                    # The player will have a starting inventory containing a weapon stick that does 4 damage, and a leather amour piece that has a defense of 2
                    player_data["inventory"] = [
                        {"name": "Stick", "type": "Weapon", "damage": 4},
                        {"name": "Leather Armor", "type": "Armor", "defense": 2}
                    ]
                    json.dump(player_data, f)
                    self.name = player_data["name"]
                    self.gold = player_data["gold"]
                    self.inventory = player_data["inventory"]
                    



    