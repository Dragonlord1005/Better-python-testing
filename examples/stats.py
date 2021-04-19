# This is a new version of stats from the combat but instead it uses classes which I hope will make things easier

class npc:
  def __init__(self, type, attack, health):
    self.type = type
    self.attack = attack
    self.health = health

  # this makes the npc take damage
  def enemy_damage(self, damage):
    self.health = self.health - damage

  # This gets the npc's health
  def enemy_health(self):
    return self.health


class player:
    def __init__(self, name, age, attack, health):
        self.name = name
        self.age = age
        self.attack = attack
        self.health = health

    # will get the name of the player
    def get_name(self):
        return self.name

    # Will get the value of attack from the player
    def get_attack(self):
        return self.attack

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
    def math_health(self, damage):
        self.health = self.health - damage


# This is for enemies, will make it inherit from another class soon
class enemy:
    def __init__(self, type, attack, health):
        self.type = type
        self.attack = attack
        self.health = health

    # this makes the enemy take damage
    def enemy_damage(self, damage):
        self.health = self.health - damage

    # This gets the enemys health
    def enemy_health(self):
        return self.health


print("What is your name?")
info = input(">")
character_name = info
print("What is your age?")
info = input(">")
character_age = info
player_info = player(character_name, character_age, 7, 50)
print(player_info.get_name(), player_info.get_age(), player_info.get_health())
player_info.math_health(7)
print("You are at", player_info.get_health(), "health")
guard = enemy("guard", 7, 50)
guard.enemy_damage(player_info.get_attack())
print("The enemy is at", guard.enemy_health(), "health")
