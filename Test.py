from random import randint
import os
import pytest


#test
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

#This is for sneaking
def stealth():
    sneak = randint(1, 10)
    if sneak == (1 or 2 or 3 or 4 or 5 or 6 or 7):
        print("You sneak past")
    elif sneak:
        print("You don't sneak past and are caught,")
        print("This would initate combat but its not done")


print("A guard stands before you")
print("you can sneak, attack, or run")
print("type your response")
option = input(">")
if option == ("sneak"):
    stealth()
if option == ("attack"):
    print("You would attack, but it's not implemented")
if option == ("run"):
    print("You run away, flailing your arms, while screaming like a coward")
if option == ("test"):
    stealth()
