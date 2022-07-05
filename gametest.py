# Random is for well combat stuff and typety is for typing
from random import randint
import typety
from tests import attack


# This is for sneaking
def stealth():
    """Defines stealth"""
    sneak = randint(1, 20)
    if sneak == (12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20):
        typety.typingprint("You sneak past\n")
    elif sneak:
        typety.typingprint("You don't sneak past and are caught,\n")
        attack.combat()


typety.typingprint("A guard stands before you\n")
typety.typingprint("you can sneak, attack, or run\n")
typety.typingprint("type your response\n")
option = input(">")
if option == ("sneak"):
    stealth()
if option == ("attack"):
    typety.typingprint("You atttack the guard, the battle begins!!!!\n")
    attack.combat()
if option == ("run"):
    typety.typingprint(
        "You run away, flailing your arms, while screaming like a coward\n"
    )
    typety.typingprint(
        "You end up attracting too much attention, and are thrown in jail\n"
    )
    typety.typingprint("You lose\n")
