from random import randint
import os
import tkinter
import PIL

#This is for sneaking
def stealth():
    sneak = randint(1, 20)
    if sneak == (12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20):
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
