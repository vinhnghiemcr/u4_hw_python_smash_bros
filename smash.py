import random


class Character:
    def __init__(self, name, moves):
        self.name = name
        self.moves = moves
        self.health = 100

    def attack(self):
        return self.moves[random.randrange(len(self.moves))]

    def get_hit(self, point):
        self.health -= point


class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def start(self):
        while self.character1.health > 0 and self.character2.health > 0:
            attack1 = self.character1.attack()
            self.character2.get_hit(attack1["damage"])
            print("{} is using {}, and damages {} {} health, remaining {} hp".format(
                self.character1.name, attack1["name"], self.character2.name, attack1["damage"], self.character2.health))
            attack2 = self.character2.attack()
            self.character1.get_hit(attack2["damage"])
            print("{} is using {}, and damages {} {} health,  remaining {} hp".format(
                self.character2.name, attack2["name"], self.character2.name, attack1["damage"], self.character1.health))

        if self.character1.health <= 0:
            print("{} is the winner".format(self.character2.name))
        else:
            print("{} is the winner".format(self.character1.name))
