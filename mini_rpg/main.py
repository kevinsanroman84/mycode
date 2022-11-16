#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import character
import json

game_over = False

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print("""
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      attack monster(if monster in room)
    """)

def show_items(items):
    items_text = ""
    for item in items:
        items_text += "[" + item + "] "
    return items_text

def showStatus():
    """determine the current status of the player"""
    current_room = rooms[player.current_room]
    # print the player's current location
    print("---------------------------")
    print("You are in the " + player.current_room)
    # print what the player is carrying
    print("Inventory:", player.inventory)
    # check if there's an item in the room, if so print it
    if current_room["item"]:
        print("You see a " + show_items(current_room["item"]))
    if "monster" in current_room:
        print("You see a monster!")

    print("---------------------------")

def game_state():
    if player.current_room == "hidden room":
        game_over = True

def new_monster(current_monster):
    if current_monster == "":
        current_monster = character.Monster()
    return  current_monster    

# a dictionary linking a room to other rooms
with open("json_data.json") as json_file:
    rooms = json.load(json_file)

# start the player in the Hall
player = character.new_player()
player.current_room = "Hall"

showInstructions()

# Placeholder for monster to remain through loops
current_monster = ""

# breaking this while loop means the game is over
while player.health > 0 and not game_over:
    showStatus()
    if "monster" in rooms[player.current_room]:
        current_monster = new_monster(current_monster)

    # the player MUST type something in
    # otherwise input will keep asking
    move = ""
    while move == "" or len(move.split(" ", 1)) < 2:
        move = input(">")
        d = len(move.split(" ", 1))

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type "go" first
    if move[0] == "go" and "monster" not in rooms[player.current_room]:
        # check that they are allowed wherever they want to go
        if move[1] in rooms[player.current_room]:
            # check if trying to go into Hidden Room
            if rooms[player.current_room][move[1]] != "Hidden Room":
                # set the current room to the new room
                player.current_room = rooms[player.current_room][move[1]]
                character.Character.player_moves += 1
            # player must have key to enter Hidden Room
            elif "key" in player.inventory:
                player.current_room = rooms[player.current_room][move[1]]
                game_over = True
            else: 
                print("You must have the key to go into the Hidden Room!")
                
        # if they aren"t allowed to go that way:
        else:
            print("You can't go that way!")

    # if they type "get" first
    if move[0] == "get" and "monster" not in rooms[player.current_room]:
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[player.current_room] and move[1] in rooms[player.current_room]["item"]:
            # add the item to their inventory
            player.inventory.append(move[1])
            # display a helpful message
            print(move[1] + " got!")
            # delete the item key:value pair from the room's dictionary
            rooms[player.current_room]["item"].remove(move[1])
        # if there"s no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print("Can't get " + move[1] + "!")

    if move[0] == "attack":
        if "monster" in rooms[player.current_room]:
            print("It's " + current_monster.name + "!!!")
            current_monster.health -= player.attack_damage(current_monster)
            print("You hit it for " + str(player.attack_damage(current_monster)) + " damage!")
            if current_monster.health <= 0:
                print("Monster died!")
                current_monster = ""
                del rooms[player.current_room]["monster"]
            else:
                player.health -= current_monster.attack_damage(player)
                print("You took " + str(current_monster.attack_damage(player))+ " damage!")
        else:
            print("No monster to attack...")
            print("You hit the wall and damage the wallpaper...")
    if move[0] != "attack" and "monster" in rooms[player.current_room]:
        current_monster = new_monster(current_monster)
        player.health -= current_monster.attack_damage(player)
        print("You took " + str(current_monster.attack_damage(player))+ " damage!")
        print("Don't ignore the monster!!!")


if player.health <= 0:
    print("GAME OVER...")
    input()
    
elif "key" in player.inventory:
    print("You escaped!")
    print("You won!!!")
    input()
