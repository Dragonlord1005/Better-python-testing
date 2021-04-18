# This is a new version of stats from the combat but instead it uses classes which I hope will make things easier
class player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


Jack = player("Jack", 50)
print(Jack.get_name(), Jack.get_age())

print("What is your name?")
info = input(">")
character_name = info
print("What is your age?")
info = input(">")
character_age = info
player_info = player(character_name, character_age)
print(player_info.get_name(), player_info.get_age())