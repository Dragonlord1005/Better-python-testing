import random
import time
import sys



# This is for typing
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value 



# This is for sneaking
def stealth():
    sneak = random.randint(1, 20)
    if sneak == (12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20):
        print("You sneak past")
    elif sneak:
        typingPrint("You don't sneak past and are caught,\n")
        typingPrint("This would initate combat but its not done\n")

typingPrint("A guard stands before you\n")
typingPrint("you can sneak, attack, or run\n")
typingPrint("type your response\n")
option = input(">")
if option == ("sneak"):
    stealth()
if option == ("attack"):
    typingPrint("You would attack, but it's not implemented\n")
if option == ("run"):
    typingPrint("You run away, flailing your arms, while screaming like a coward\n")
    typingPrint("You end up attracting too much attention, and are thrown in jail\n")
    typingPrint("You lose\n")
if option == ("test"):
    stealth()
