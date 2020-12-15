from smash import Smash_Char, Battle
import characters
import random
import time
from pprint import pprint


all_characters = [Smash_Char(char['name'], char['attacks'])
                  for char in characters.characters]

char_dict = {}
char_available = {}

my_opponent = None
my_char = None

for i, char in enumerate(all_characters):
    char_dict.update({i: char.char_name})
    char_available.update({i: char})


def fight_start_timer(player, comp):
    print("{player} VS {comp}".format(player=player, comp=comp))
    timers = [i for i in range(1, 6)]
    for i in timers[::-1]:
        print("Fight Starting in: {el_time}".format(el_time=i))
        time.sleep(1)


def select_chars():
    pprint(char_dict)
    my_char = None
    player_choice = input('Select a character from the above list. ')
    if player_choice:
        my_char = char_available[int(player_choice)]
    else:
        my_char = random.choice(all_characters)
    print("You Chose: {charname}".format(charname=my_char.char_name.upper()))
    my_opponent = random.choice(all_characters)
    print("Your Opponent: {op_name}".format(
        op_name=my_opponent.char_name.upper()))
    return (my_char, my_opponent)


def play_game(player, comp_player):
    round_num = 1
    fight = Battle()
    print('{player} vs {comp}'.format(
        player=player.char_name, comp=comp_player.char_name))

    while player.has_life or comp_player.has_life:
        print("Round {round}, FIGHT!".format(round=round_num))
        dmg = fight.start(comp_player, player)
        if dmg >= comp_player.char_health:
            print('You Win')
            break
        comp_player.decrement_health(dmg)
        op_dmg = fight.start(player, comp_player)
        if op_dmg >= player.char_health:
            print('You Lose')
            break
        player.decrement_health(op_dmg)
        time.sleep(2)
        round_num += 1


players = select_chars()
fight_start_timer(players[0].char_name, players[1].char_name)
play_game(players[0], players[1])
