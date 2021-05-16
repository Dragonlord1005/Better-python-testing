# Random is for well combat stuff and typey is for typing
from random import randint
from tests import typey
from tests import attack


# This is for sneaking
def stealth():
    '''Defines stealth'''
    sneak = randint(1, 20)
    if sneak == (12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20):
        typey.typingprint("You sneak past\n")
    elif sneak:
        typey.typingprint("You don't sneak past and are caught,\n")
        attack.combat()


typey.typingprint("A guard stands before you\n")
typey.typingprint("you can sneak, attack, or run\n")
typey.typingprint("type your response\n")
option = input(">")
if option == ("sneak"):
    stealth()
if option == ("attack"):
    typey.typingprint("You atttack the guard, the battle begins!!!!\n")
    attack.combat()
if option == ("run"):
    typey.typingprint(
        "You run away, flailing your arms, while screaming like a coward\n")
    typey.typingprint(
        "You end up attracting too much attention, and are thrown in jail\n")
    typey.typingprint("You lose\n")
