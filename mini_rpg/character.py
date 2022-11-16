import random

monster_names = ["the Cavernfang"
"the Foulpest",
"the Stonevine",
"the Vexsword",
"the Putrid Horror",
"the Lone Body",
"the Angry Gnoll",
"the Evasive Vision Serpent",
"the Mad Mist Buffalo",
"the Silver Killer Beast"]

# Player creation
def new_player():
    player_name = input("What is your name??? \n> ")
    while not player_name:
        player_name = input("What is your name??? \n> ")

    valid_classes = ["rogue", "barbarian", "wizard", "paladin"]
    print("Rogue = bonus damage for surprise attacks.")
    print("Barbarian = bonus damage when health is low.")
    print("Wizard = bonus damage if you are faster than monster.")
    print("Paladin = bonus damage if you have more defense than monster.")
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
    def __init__(self, name):
        super().__init__(name)
        self.health = 10
        self.attack = 25
        self.defense = 5
        self.speed = 5

    def attack_damage(self, target):
        damage = super().attack_damage(target)
        if self.health <= 5:
            return damage * 3
        return damage

        
class Wizard(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 10
        self.attack = 23
        self.defense = 5
        self.speed = 8

    def attack_damage(self, target):
        damage = super().attack_damage(target)
        if target.speed <= self.speed:
            return damage * 3
        return damage

class Paladin(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 15
        self.attack = 15
        self.defense = 15
        self.speed = 5
        
    def attack_damage(self, target):
        damage = super().attack_damage(target)
        if target.defense <= self.defense:
            return damage * 3
        return damage

# Class for monsters to fight
class Monster(Character):
    def __init__(self):
        super().__init__(random.choice(monster_names))
        self.health = random.randint(5, 5 + Character.player_moves)
        self.attack = random.randint(5, 5 + Character.player_moves)
        self.defense = random.randint(5, 5 + Character.player_moves)
        self.speed = random.randint(5, 5 + Character.player_moves)
        self.is_aware = False

    def attack_damage(self, target):
        damage = super().attack_damage(target)
        # reduce monsters attack to only 5 damage
        if damage >= 5:
            return 5
        return damage