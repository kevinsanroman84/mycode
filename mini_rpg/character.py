class Character():
    def __init__(self, name):
        self.name = name
        self.health = 1
        self.attack = 1 
        self.defense = 1
        self.speed = 1
    
    # Checks targets defense and your attack for damage.
    def attack(self, target):
        return
    
class Player(Character):
    def __init__(self, name, job):
        self.job = job

    Person.__init__(self, name)