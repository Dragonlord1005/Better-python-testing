# This is a new version of stats from the combat but instead it uses classes which I hope will make things easier
class player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health


Jack = player("Jack", 50)
print(Jack.get_name(), Jack.get_health())
