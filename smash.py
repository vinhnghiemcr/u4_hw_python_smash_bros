import random


class Battle:

    def start(self, target, attacker):
        attack_move = random.choice(attacker.attacks)
        print("{attacker_name} used {attack_name} and inflicted {damage} damage!".format(
            attacker_name=attacker.char_name, attack_name=attack_move['name'], damage=attack_move['damage']))
        return attack_move['damage']


class Smash_Char(Battle):
    def __init__(self, char_name: str, attacks: list):
        self.char_name = char_name
        self.char_health = 100
        self.attacks = attacks
        self.has_life = True

    def decrement_health(self, amount: int):
        if self.char_health <= amount:
            self.char_health = 0
            self.has_life = False
        else:
            self.char_health -= amount
            round(self.char_health, 1)

        print("{name} has {health} health points remaining!".format(
            name=self.char_name, health=self.char_health))
