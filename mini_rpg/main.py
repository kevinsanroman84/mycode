#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import character


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print("""
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    """)


def showStatus():
    """determine the current status of the player"""
    # print the player"s current location
    print("---------------------------")
    print("You are in the " + player.current_room)
    # print what the player is carrying
    print("Inventory:", player.inventory)
    # check if there"s an item in the room, if so print it
    if "item" in rooms[player.current_room]:
        print("You see a " + rooms[player.current_room]["item"])
    print("---------------------------")


# a dictionary linking a room to other rooms
rooms = {
    "Hall": {
        "south": "Kitchen",
        "east": "Dining Room",
        "item": "key"
    },

    "Kitchen": {
        "north": "Hall",
        "item": "monster",
    },
    "Dining Room": {
        "west": "Hall",
        "south": "Garden",
        "item": "potion"
    },
    "Garden": {
        "north": "Dining Room"
    }
}

# start the player in the Hall
player = character.new_player()
player.current_room = "Hall"

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ""
    while move == "":
        move = input(">")

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type "go" first
    if move[0] == "go":
        # check that they are allowed wherever they want to go
        if move[1] in rooms[player.current_room]:
            # set the current room to the new room
            player.current_room = rooms[player.current_room][move[1]]
        # if they aren"t allowed to go that way:
        else:
            print("You can\"t go that way!")

    # if they type "get" first
    if move[0] == "get":
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[player.current_room] and move[1] in rooms[player.current_room]["item"]:
            # add the item to their inventory
            player.inventory.append(move[1])
            # display a helpful message
            print(move[1] + " got!")
            # delete the item key:value pair from the room"s dictionary
            del rooms[player.current_room]["item"]
        # if there"s no item in the room or the item doesn"t match
        else:
            # tell them they can"t get it
            print("Can\"t get " + move[1] + "!")
