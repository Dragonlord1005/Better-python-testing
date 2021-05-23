# This is a new version of stats from the
# combat but instead it uses classes which I hope will
#  make things easier
import sys


class npc:
    '''Defines the class for the NPC'''
    def __init__(self, race, attack, health):
        self.race = race
        self.attack = attack
        self.health = health

    def enemy_damage(self, damage):
        '''This makes the NPC take damage'''
        self.health = self.health - damage

    def enemy_health(self):
        '''This gets the npc's health'''
        return self.health


class player:
    '''Defines the class for the player'''
    def __init__(self, name, age, attack, health):
        self.name = name
        self.age = age
        self.attack = attack
        self.health = health

    def get_name(self):
        '''Will get the name of the player'''
        return self.name

    def get_attack(self):
        '''Will get the value of attack from the player'''
        return self.attack

    def get_age(self):
        '''Will get the age of the player'''
        return self.age

    def get_health(self):
        '''Will grab healths value from player'''
        return self.health

    def set_health(self, health):
        '''Sets health for player, don't know what to use it for yet'''
        self.health = health

    def math_health(self, damage):
        '''This subtracts health from the player, need to get it to take input'''
        self.health = self.health - damage


class enemy:
    '''This is for enemies, will make it inherit from another class soon'''
    def __init__(self, monster, attack, health):
        self.monster = monster
        self.attack = attack
        self.health = health

    def enemy_damage(self, damage):
        '''This makes the enemy take damage'''
        self.health = self.health - damage

    def enemy_health(self):
        '''This gets the enemys health'''
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
sys.stdout.write("The enemy is at")
sys.stdout.write(str(guard.enemy_health()))
sys.stdout.write(" health")
