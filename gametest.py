# We must initialize the game itself in its entirety
# We will use the player class to create the player
# We will use the inventory class to create the inventory
# We will use the combat class to create the combat
# We will need to import the ability to read and write to json files
# We will use the ability to read and write to json files to save the player data

import json
# We will need to import all the necessary classes, these can be found in the src directory
from player import Player
from inventory import Inventory, Item, Weapon, Armor
from combat import Combat

# The player will be able to choose their name at the beginning of the game, and it must be saved to a local file, along with other player information, such as gold, inventory, weapon damage, armor defense
# The player will have a starting gold of 300
# The player will have a starting inventory containing a stick that does 4 damage, and a leather amour piece that has a defense of 2
# The player information will be stored in playerdata.json in the json format and will be loaded when the game starts


# We will need to create a class for the game
class Game:
    """Defines the game class"""

    def __init__(self):
        """Initializes the game class"""
        self.player = Player("", 0, Inventory()) # Initializes the player class
        self.combat = Combat() # Initializes the combat class
        self.load_player() # Loads the player data
        self.load_inventory() # Loads the inventory data
        self.load_combat() # Loads the combat data

    