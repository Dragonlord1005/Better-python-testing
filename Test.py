import pytest
print("A guard stands before you")
print("you can sneak, attack, or run")
print("type your response")
option = input(">>>")
if option == ("sneak"):
    print("You sneak past")
if option == ("attack"):
  print("You would attack, but it's not implemented")
if option == ("run"):
  print("You run away, flailing your arms, while screaming like a coward")