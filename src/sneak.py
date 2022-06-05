def stealth():
    """Defines stealth, needs no additional arguments."""
    sneak = random.randint(1, 10) # Chance is between 1 and 10
    if sneak == (1 or 2 or 3 or 4 or 5): # If the Stealth is 1-5 then the player is not detected
        print("You sneak past")
    elif sneak: == (6 or 7 or 8 or 9 or 10): # If the Stealth is 6-10 then the player is detected
        print("You don't sneak past and are caught,") 
        print("this does nothing in the example") 
