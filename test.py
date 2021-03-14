import random
import time
import sys


# This is for combat
player_health = 50
player_attack = 7
player_defending = 0
enemy_health = 50
enemy_attack = 7
enemy_defending = 0
turn = 0
enemy_choice = 0
winner = 3
battling = 0

while battling == 1:
  #this is for player attacking
  def attack():
    if enemy_defending == 0:
      enemy_health = enemy_health - player_attack
    elif enemy_defending == 1:
      enemy_health = enemy_health - (player_attack / 2)
      enemy_defending = 0
      turn = 1
    typingPrint("you successfully attacked\n")
    print("the enemy is now at", enemy_health, "health!!!")
    turn = 1
  #this is for player defending
  def defend():
    globals()
    global player_defending
    player_defending = 1
    turn = 1
  if turn == 0:
    typingPrint("You can attack or defend\n")
    battle = input(">")
  if battle == ("attack"):
    attack()
  if battle == ("defend"):
    defend()
  if battle == ("debug"):
    turn = 1
  #this is for the enemys turn
  if turn == 1:
    enemy_choice = random.randint(1, 10)
    print("works")
    if enemy_choice == (1 or 2 or 3 or 4 or 5):
      typingPrint("the enemy is going to attack you!\n")
      if player_defending == 0:
        player_health = player_health - enemy_attack
    elif player_defending == 1:
      player_health = player_health - (enemy_attack / 2)
      player_defending = 0
    elif enemy_choice:
      enemy_defending = 1
      typingPrint("The enemy is defending\n")
    print("You are now at", player_health, "health!!!!")
    turn = 0


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
  typingPrint("You atttack the guard, the battle begins!!!!\n")
  battling = 1
if option == ("run"):
    typingPrint("You run away, flailing your arms, while screaming like a coward\n")
    typingPrint("You end up attracting too much attention, and are thrown in jail\n")
    typingPrint("You lose\n")
if option == ("test"):