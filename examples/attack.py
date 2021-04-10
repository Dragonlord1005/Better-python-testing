# this is the combat module
from numba import jit, njit


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
  "winner": 3
}
win = info["winner"]
while win == 0:
  # this is for player attacking
  def attack():
      enemy_defending = info["enemy_defending"]
    if info["enemy_defending"] = 0:
        print("hey")
    dlif enemy_defending == 1:
      enemy_health = enemy_health - (player_attack / 2)
      enemy_defending = 0
    turn = 1
    print("you successfully attacked")
    print("the enemy is now at", enemy_health, "health!")

  # this is for player defending
  def defend():
    turn = 1

    if turn == 0:
        print("You can attack or defend")
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
                print("the enemy is going to attack you!")
                if player_defending == 0:
                    player_health = player_health - enemy_attack
                elif player_defending == 1:
                    player_health = player_health - (enemy_attack / 2)
                    player_defending = 0
            elif enemy_choice:
                enemy_defending = 1
                print("The enemy is defending\n")
            print("You are now at", player_health, "health!!!!")
            turn = 0
info["winner"] = 0
