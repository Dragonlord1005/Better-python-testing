# Make a turn based combat system
# The Player, and the enemy (there can be multiple enemies) each take turns attacking, each turn, the player can choose to attack or defend, on the enemies turn, there is a 50-50 chance the enemy will attack or defend
# If the player or enemy defends, the attack is reduced by the value of the defense
# If the player or enemy attacks, the attack is increased by the value of the attack, where the base value is zero
# We will be using classes to do this to allow for more complex combat
# The enemy and player classes will be in seperate files
# The player class will be in the player.py file
# The enemy class will be in the enemy.py file
# All item and inventory classes are in the inventory.py file
# The order of combat is based off the dexterity of the player and the dexterity of the enemy, the higher the dexterity, the earlier the player or enemy takes their turn
# If the player and enemy dexterity are the same, the player goes first

class Combat:
    """Defines combat class"""
    
        def __init__(self, player, enemy):
            """Initializes the combat class"""
            self.player = player # Sets the player
            self.enemy = enemy # Sets the enemy
            self.turn = 0 # Initializes the turn
            self.player_turn = True