import random
import pygradle


#This is for sneaking
def stealth():
    sneak = random.randint(1, 5)
    if sneak == [1 or 2 or 3 or 4 or 5]:
        print(sneak)


print("A guard stands before you")
print("you can sneak, attack, or run")
print("type your response")
option = input(">")
if option == ("sneak"):
    print("You sneak past")
if option == ("attack"):
    print("You would attack, but it's not implemented")
if option == ("run"):
    print("You run away, flailing your arms, while screaming like a coward")
if option == ("test"):
    stealth()
