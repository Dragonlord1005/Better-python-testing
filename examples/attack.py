# this is the combat module
from random import randint

# This is for combat
info = {
    "player_health": 50,
    "player_attack": 7,
    "player_defending": 0,
    "enemy_health": 50,
    "enemy_attack": 7,
    "enemy_defending": 0,
    "turn": 0,
    "enemy_choice": 0,
    "winner": 0
}


def combat():
    info["winner"] = 3
    while info["winner"] == 3:
        # this is for player attacking
        def attack():
            enemy_defending = info["enemy_defending"]
            if enemy_defending == 0:
                print("hey")
            elif enemy_defending == 1:
                info["enemy_health"] = info[
                    "enemy_health"] - info["player_attack"] / 2
                info["enemy_defending"] = 0
            info["turn"] = 1
            print("you successfully attacked")
            print("the enemy is now at", info["enemy_health"], "health!")

        # this is for player defending
        def defend():
            info["turn"] = 1

        if info["player_health"] <= 0:
            print("You lose, keep trying!")
            info["winner"] = 2
            break
        if info["enemy_health"] <= 0:
          print("you win, this doesnt progress the story yet")
          info["winner"] = 1
          break

        if info["turn"] == 0:
            print("You can attack or defend")
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
            print("works")
            if info["enemy_choice"] == (1 or 2 or 3 or 4 or 5):
                print("the enemy is going to attack you!")
                if info["player_defending"] == 0:
                    info["player_health"] = info["player_health"] - info["enemy_attack"]
                elif info["player_defending"] == 1:
                    info["player_health"] = info[
                        "player_health"] - info["enemy_attack"] / 2
                    info["player_defending"] = 0
            elif info["enemy_choice"]:
                info["enemy_defending"] = 1
                print("The enemy is defending")
            print("You are now at", info["player_health"], "health!!!!")
            info["turn"] = 0

combat()
