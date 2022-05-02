import random
import json
from smash import Character, Battle
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def find_character(name):
    for character in characters:
        if character["name"].lower() == name.lower():
            return character
    return None


def play():
    player_character = {}
    player_choice = input("Enter your character's name: ")
    if player_choice:
        player_character = find_character(player_choice)
    else:
        player_character = random.choice(characters)
    print("You choose {}".format(player_character["name"]))
    comp_character = random.choice(characters)
    print("Computer choose {}".format(comp_character['name']))
    player = Character(player_character["name"], player_character["attacks"])
    comp = Character(comp_character["name"], comp_character["attacks"])
    print(player.name)
    print(comp.name)

    battle = Battle(player, comp)
    battle.start()


play()
