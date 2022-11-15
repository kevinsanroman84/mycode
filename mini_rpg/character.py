

# Classes for players, monsters, and npcs
class Character():
    def __init__(self, name, health=1, attack=1, defense=1, speed=1):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
    # Checks targets defense and your attack for damage.
    def attack(self, target):
        return

# Specific attributes and classes for the player character
class Player(Character):
    def __init__(self, name, health, attack, defense, speed):
        Character.__init__(self, name)
        self.moves = 0

# Job classes for specific stats for players
class Rogue(Player):
    def __init__(self, name, health=1, attack=1, defense=1, speed=1):
        Player.__init__(self, name, health, attack, defense, speed)

class Barbarian(Player):
    def __init__(self, name, health, attack, defense, speed):
        Player.__init__(name, health, attack, defense, speed)

class Wizard(Player):
    def __init__(self, name, health, attack, defense, speed):
        Player.__init__(name, health, attack, defense, speed)

class Paladin(Player):
    def __init__(self, name, health, attack, defense, speed):
        Player.__init__(name, health, attack, defense, speed)