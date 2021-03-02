# This is purely for testing purposes and may not be final
player_health = 50
player_attack = 7
enemy_health = 50
enemy_attack = 7

def attack():
  global enemy_health
  enemy_health = enemy_health - 7
  print("you successfully attacked")
  print(enemy_health)
  

print("You can attack or defend")
print("defending is not implemented")
battle = input(">")

if battle == ("attack"):
  attack()
