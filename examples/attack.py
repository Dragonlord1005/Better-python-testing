# This is purely for testing purposes and may not be final
import time
import sys


#this is for typing effect
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)




player_health = 50
player_attack = 7
enemy_health = 50
enemy_attack = 7

def attack():
  global enemy_health
  enemy_health = enemy_health - 7
  typingPrint("you successfully attacked\n")
  print("the enemy is now at", enemy_health, "health!!!")
  
  
  

typingPrint("You can attack or defend\n")
typingPrint("defending is not implemented\n")
battle = input(">")

if battle == ("attack"):
  attack()
