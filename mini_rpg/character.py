import random

monster_names = ["Cavernfang"
"Foulpest",
"Stonevine",
"Vexsword",
"The Putrid Horror",
"The Lone Body",
"The Angry Gnoll",
"The Evasive Vision Serpent",
"The Mad Mist Buffalo",
"The Silver Killer Beast"]

# Player creation
def new_player():
    player_name = input("What is your name??? \n> ")
    while not player_name:
        player_name = input("What is your name??? \n> ")

    valid_classes = ["rogue", "barbarian", "wizard", "paladin"]
    player_class = input(
        "What is your job? [Rogue] [Barbarian] [Wizard] [Paladin]\n> ").lower()
    while player_class not in valid_classes:
        player_class = input(
            "What is your job? [Rogue] [Barbarian] [Wizard] [Paladin]\n> ")
    if player_class == "rogue":
        player = Rogue(player_name)
    elif player_class == "barbarian":
        player = Barbarian(player_name)
    elif player_class == "wizard":
        player = Wizard(player_name)
    elif player_class == "paladin":
        player = Paladin(player_name)

    return player


# Classes for players, monsters, and npcs
class Character():
    player_moves = 0
    def __init__(self, name, health=1, attack=1, defense=1, speed=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
    # Checks stats for damage modifiers 
    def attack_damage(self, target):
        damage = self.attack - target.defense
        if damage < 1:
            return 1
        return damage

# Specific attributes and classes for the player character
class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = []
        self.current_room = ""

    # Takes you to starting room
    def teleport(self):
        return

    # Checks room according to job class  
    def inspect(self):
        pass

# Job classes for specific stats for players
class Rogue(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 10
        self.attack = 15
        self.defense = 5
        self.speed = 15

    def attack_damage(self, target):
        damage = super().attack_damage(target)
        if target.is_aware:
            return damage
        return damage * 3


class Barbarian(Player):
    def __init__(self, name, health=10, attack=25, defense=5, speed=5):
        super().__init__(name, health, attack, defense, speed)

    def attack_damage(self, target):
        damage = super().attack_damage(target)
        if self.health <= 5:
            return damage * 3
        return damage

        
class Wizard(Player):
    def __init__(self, name, health=10, attack=23, defense=5, speed=8):
        super().__init__(name, health, attack, defense, speed)


class Paladin(Player):
    def __init__(self, name, health=15, attack=15, defense=15, speed=5):
        super().__init__(name, health, attack, defense, speed)


# Class for monsters to fight
class Monster(Character):
    def __init__(self):
        super().__init__(random.choice(monster_names))
        self.health = random.randint(5, 5 + Character.player_moves)
        self.attack = random.randint(5, 5 + Character.player_moves)
        self.defense = random.randint(5, 5 + Character.player_moves)
        self.speed = random.randint(5, 5 + Character.player_moves)
        self.is_aware = False
