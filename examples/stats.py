# This is a new version of stats from the combat but instead it uses classes which I hope will make things easier
class player:
    def __init__(self, name, age, attack, health):
        self.name = name
        self.age = age
        self.attack = attack
        self.health = health

    # will get the name of the player
    def get_name(self):
        return self.name

    # will get the age of the player
    def get_age(self):
        return self.age

    # Will grab healths value from player
    def get_health(self):
        return self.health

    # Sets health for player, don't know what to use it for yet
    def set_health(self, health):
        self.health = health

    # This subtracts health from the player, need to get it to take input
    def math_health(self):
        self.health = self.health - 7


# This is for enemies, it's not finished, I dont know if it works yet
class enemy:
    def __init__(self, type, attack, health):
        self.type = type
        self.attack = attack
        self.health = health
    def enemy_damage(self, target):
      self.health = self.health - target


print("What is your name?")
info = input(">")
character_name = info
print("What is your age?")
info = input(">")
character_age = info
player_info = player(character_name, character_age, 7, 50)
print(player_info.get_name(), player_info.get_age(), player_info.get_health())
player_info.set_health(8)
print(player_info.get_health())
print(player_info.math_health())
print(player_info.get_health())
