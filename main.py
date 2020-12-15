from smash import Smash_Char, Battle
import characters
import random
import time

all_characters = [Smash_Char(char['name'], char['attacks'])
                  for char in characters.characters]


my_char = random.choice(all_characters)

my_opponent = random.choice(all_characters)

round_num = 1
fight = Battle()
print('{player} vs {comp}'.format(
    player=my_char.char_name, comp=my_opponent.char_name))

while my_char.has_life or my_opponent.has_life:
    print("Round {round}, FIGHT!".format(round=round_num))
    dmg = fight.start(my_opponent, my_char)
    if dmg >= my_opponent.char_health:
        print('You Win')
        break
    my_opponent.decrement_health(dmg)
    op_dmg = fight.start(my_char, my_opponent)
    if op_dmg >= my_char.char_health:
        print('You Lose')
        break
    my_char.decrement_health(op_dmg)
    time.sleep(1)
    round_num += 1
