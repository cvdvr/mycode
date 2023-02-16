#!/usr/bin/python3

import random

# Define the player's starting stats
player_name = input("What is your character's name? ")
player_health = 20
player_strength = 10
player_gold = 0

# Define the different paths in the dungeon
paths = {
    "start": ["left", "straight", "right"],
    "left": ["goblins", "treasure"],
    "straight": ["healing", "trap"],
    "right": ["minotaur", "door"],
    "door": ["treasure", "skeleton"]
}

# Create a list to store the paths the player has already taken
taken_paths = []

# Welcome message to the game
print(f"Welcome, {player_name}, to the world of Dungeons and Dragons! Your journey begins now.")

# First prompt with 3 paths to choose from
print("You find yourself in a dark dungeon with 3 paths. Which path do you choose?")
print("1. The path to the left")
print("2. The path straight ahead")
print("3. The path to the right")

# Get user input for the first prompt
prompt = int(input("Enter the number of your choice: "))

# Check the user's input and determine the outcome
if prompt == 1:
    if "goblins" not in taken_paths:
        print("You encounter a group of goblins. Roll to attack.")
        goblin_health = 5
        while goblin_health > 0 and player_health > 0:
            player_roll = random.randint(1, 20) + player_strength
            goblin_roll = random.randint(1, 20)
            if player_roll > goblin_roll:
                damage = random.randint(1, 6) + player_strength
                goblin_health -= damage
                print(f"You hit the goblin for {damage} damage. The goblin has {goblin_health} health remaining.")
            else:
                damage = random.randint(1, 4)
                player_health -= damage
                print(f"The goblin hits you for {damage} damage. You have {player_health} health remaining.")
        if player_health > 0:
            print("You defeated the goblins and find a treasure chest. You gain 10 gold.")
            player_gold += 10
            taken_paths.append("goblins")
        else:
            print("You were defeated by the goblins. Game over.")
            exit()
    else:
        print("You've already been down this path.")
        
elif prompt == 2:
    if "healing" not in taken_paths:
        print("You find a healing potion on the ground. You gain 5 health.")
        player_health += 5
        taken_paths.append("healing")
    else:
        print("You've already been down this path.")
        
elif prompt == 3:
    if "minotaur" not in taken_paths:
        print("You encounter a minotaur. Roll to attack.")
        minotaur_health = 15
        while minotaur_health > 0 and player_health > 0:
            player_roll = random.randint(1, 20) + player_strength
            minotaur_roll = random.randint(1, 20)
            if player_roll > minotaur_roll:
                damage = random.randint(1, 8) + player_strength
                minotaur_health -= damage
                print(f"You hit the minotaur for {damage} damage. The minotaur has {minotaur_health} health remaining.")
            else:
                damage

