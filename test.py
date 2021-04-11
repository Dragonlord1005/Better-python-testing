import random

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

while info["winner"] >= 3:
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

    if info["turn"] == 0:
        print("You can attack or defend")
        battle = input(">")
        if battle == ("attack"):
            attack()
        if battle == ("defend"):
            defend()
        if battle == ("debug"):
            turn = 1
        if battle == ("win"):
            info["winner"] = 5
            # this is for the enemys turn
    if info["turn"] == 1:
        info["enemy_choice"] = random.randint(1, 10)
        print("works")
        if info["enemy_choice"] == (1 or 2 or 3 or 4 or 5):
            print("the enemy is going to attack you!")
            if info["player_defending"] == 0:
                info["player_health"] = ["player_health"
                                         ] - info["enemy_attack"]
            elif info["player_defending"] == 1:
                info["player_health"] = info[
                    "player_health"] - info["enemy_attack"] / 2
                indo["player_defending"] = 0
        elif info["enemy_choice"]:
            info["enemy_defending"] = 1
            print("The enemy is defending")
        print("You are now at", info["player_health"], "health!!!!")
        info["turn"] = 0


# This is for sneaking
def stealth():
    sneak = random.randint(1, 20)
    if sneak == (12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20):
        print("You sneak past")
    elif sneak:
        print("You don't sneak past and are caught,\n")
        print("This would initate combat but its not done\n")


print("A guard stands before you\n")
print("you can sneak, attack, or run\n")
print("type your response\n")
option = input(">")
if option == ("sneak"):
    stealth()
if option == ("attack"):
    print("You atttack the guard, the battle begins!!!!")
    info["winner"] = 3
if option == ("run"):
    print("You run away, flailing your arms, while screaming like a coward\n")
    print("You end up attracting too much attention, and are thrown in jail\n")
    print("You lose\n")
