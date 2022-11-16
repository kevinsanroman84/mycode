import character
import json


rooms = {
    "Hall": {
        "south": "Kitchen",
        "east": "Dining Room",
        "item": ["scroll", "chair"], 
        "monster": "monster"
    },
    "Kitchen": {
        "north": "Hall",
        "south": "Storage Room",
        "item": ["small chest"],
    },
    "Storage Room": {
        "north": "Kitchen",
        "south": "Basement", 
        "monster": "monster",
        "item": []
    },
    "Basement": {
        "north": "Storage Room",
        "east": "Crawlspace",
        "item": []
    },
    "Crawlspace": {
        "west": "Basement", 
        "east": "Caverns", 
        "monster": "monster",
        "item": []
    },
    "Caverns": {
        "west": "Crawlspace", 
        "item": ["key"]
    },
    "Dining Room": {
        "west": "Hall",
        "south": "Garden",
        "item": ["potion"]
    },
    "Garden": {
        "north": "Dining Room",
        "south": "Hidden Room",
        "item": ["bucket", "mop"], 
        "monster": "monster"
    },
    "Hidden Room": {
        "north": "Garden", 
        "item": ["prize"]
    }
}
with open("json_data.json", "w") as json_file:
     json.dump(rooms, json_file)



player = character.Rogue("Kevin")
character.Character.player_moves = 200

monster = character.Monster()


print(player.attack_damage(monster))

