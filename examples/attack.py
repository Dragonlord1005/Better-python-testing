#this is the combat module
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


def combat():

    global enemy_health
    global winner
    while winner < 5:
        global enemy_defending
        global turn

        # this is for player attacking

        def attack():
            global enemy_defending
            global enemy_attack
            global enemy_choice
            global enemy_health
            global turn
            if enemy_defending == 0:
                enemy_health = enemy_health - player_attack
            elif enemy_defending == 1:
                enemy_health = enemy_health - (player_attack / 2)
                enemy_defending = 0
                turn = 1
            typingPrint("you successfully attacked\n")
            print("the enemy is now at", enemy_health, "health!!!")
            turn = 1

        # this is for player defending

        def defend():
            print("hi")
            globals()
            global turn
            global player_defending
            player_defending = 1
            print("You are defendig")
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
        if battle == ("win"):
            winner = 5
        # this is for the enemys turn
        if turn == 1:
            global enemy_choice
            global enemy_defending
            global enemy_attack
            global player_health
            global player_defending
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


battling = 0

while battling == 1:
    # this is for player attacking
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

    # this is for player defending

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
    # this is for the enemys turn
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
