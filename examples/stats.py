# This is a new version of stats from the combat but instead it uses classes which I hope will make things easier
class player:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health


Jack = player("Jack", 37, 50)
print(Jack.get_name(), Jack.get_age())

print("What is your name?")
info = input(">")
character_name = info
print("What is your age?")
info = input(">")
character_age = info
player_info = player(character_name, character_age, 50)
print(player_info.get_name(), player_info.get_age(), player_info.get_health())

player_info.set_health(8)
print(player_inf0.get_health)
