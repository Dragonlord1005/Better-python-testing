# Random is for well combat stuff and typey is for typing
from random import randint
import typey


# This is for combat
info = {
    "player_health": 50,
    "player_attack": 7,
    "player_defending": 0,
    "enemy_health": 30,
    "enemy_attack": 7,
    "enemy_defending": 0,
    "turn": 0,
    "enemy_choice": 0,
    "winner": 0
}


# The actual combat system (could this be redone into a module?)
def combat():
    info["winner"] = 3
    while info["winner"] == 3:
        # this is for player attacking
        def attack():
            enemy_defending = info["enemy_defending"]
            if enemy_defending == 0:
                info["enemy_health"] = info["enemy_health"] - info[
                    "player_attack"]
            elif enemy_defending == 1:
                info["enemy_health"] = info[
                    "enemy_health"] - info["player_attack"] / 2
                info["enemy_defending"] = 0
            typey.typingprint("you successfully attacked")
            typey.typingprint(" the enemy is now at ")
            typey.typingprint(str(info["enemy_health"]))
            typey.typingprint(" health!!!\n")
            info["turn"] = 1

        # this is for player defending
        def defend():
            typey.typingprint("you are defending\n")
            info["turn"] = 1

        if info["player_health"] <= 0:
            typey.typingprint("You lose, keep trying!\n")
            info["winner"] = 2
            break
        if info["enemy_health"] <= 0:
            typey.typingprint("you win, this doesnt progress the story yet\n")
            info["winner"] = 1
            break

        if info["turn"] == 0:
            typey.typingprint("You can attack or defend\n")
            battle = input(">")
            if battle == ("attack"):
                attack()
            if battle == ("defend"):
                defend()
            if battle == ("debug"):
                info["turn"] = 1
            if battle == ("win"):
                info["enemy_health"] = -1
            if battle == ("lose"):
                info["player_health"] = -15
            # this is for the enemys turn
        if info["turn"] == 1:
            info["enemy_choice"] = randint(1, 10)
            if info["enemy_choice"] == (1 or 2 or 3 or 4 or 5):
                typey.typingprint("the enemy is going to attack you!\n")
                if info["player_defending"] == 0:
                    info["player_health"] = info["player_health"] - info[
                        "enemy_attack"]
                elif info["player_defending"] == 1:
                    info["player_health"] = info[
                        "player_health"] - info["enemy_attack"] / 2
                    info["player_defending"] = 0
            elif info["enemy_choice"]:
                info["enemy_defending"] = 1
                typey.typingprint("The enemy is defending\n")
            typey.typingprint("You are now at ")
            typey.typingprint(str(info["player_health"]))
            typey.typingprint(" health!!!\n")
            info["turn"] = 0


# This is for sneaking
def stealth():
    sneak = randint(1, 20)
    if sneak == (12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20):
        typey.typingprint("You sneak past\n")
    elif sneak:
        typey.typingprint("You don't sneak past and are caught,\n")
        combat()


typey.typingprint("A guard stands before you\n")
typey.typingprint("you can sneak, attack, or run\n")
typey.typingprint("type your response\n")
option = input(">")
if option == ("sneak"):
    stealth()
if option == ("attack"):
    typey.typingprint("You atttack the guard, the battle begins!!!!\n")
    combat()
if option == ("run"):
    typey.typingprint(
        "You run away, flailing your arms, while screaming like a coward\n")
    typey.typingprint(
        "You end up attracting too much attention, and are thrown in jail\n")
    typey.typingprint("You lose\n")
