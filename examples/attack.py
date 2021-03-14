# This is purely for testing purposes and may not be final
import time
import sys
import random


#this is for typing effect
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


player_health = 50
player_attack = 7
player_defending = 0
enemy_health = 50
enemy_attack = 7
enemy_defending = 0
turn = 0
enemy_choice = 0

def combat():
  while player_health or enemy_health == 0:
    #this is for player attacking
      def attack():
        global enemy_health
        global turn
        global enemy_defending
        if enemy_defending == 0:
          enemy_health = enemy_health - player_attack
        elif enemy_defending == 1:
          enemy_health = enemy_health - (player_attack / 2)
          enemy_defending = 0
        typingPrint("you successfully attacked\n")
        print("the enemy is now at", enemy_health, "health!!!")
        turn = 1
    #this is for player defending
      def defend():
        global turn
        global player_defending
        player_defending = 1
        turn = 1

      if turn == 0:
        typingPrint("You can attack or defend\n")
        battle = input(">")

        if battle == ("attack"):
            attack()
        elif battle == ("defend"):
            defend()
        elif battle == ("debug"):
          enemy_health = 0
    #this is for the enemys turn
      if turn == 1:
        enemy_choice = random.randint(1, 10)
        if enemy_choice == (1 or 2 or 3 or 4 or 5):
            typingPrint("the enemy is going to attack you!\n")
            if player_defending == 0:
                player_health = player_health - enemy_attack
            elif player_defending == 1:
              player_health = player_health - (enemy_attack / 2)
              player_defending = 0
        elif enemy_choice == (6 or 7 or 8 or 9 or 10):
          enemy_defending = 1
          typingPrint("The enemy is defending\n")
          turn = 0

        print("You are now at", player_health, "health!!!!")
        turn = 0
      if player_health or enemy_health <= 0:
        break

combat()