import requests
import json
import re
import math
characters_request = requests.get(
    'https://api.kuroganehammer.com/api/characters').json()


char_request_data = []

for char in characters_request:
    char_request_data.append({"name": char['Name'], "link": list(filter(
        lambda link: link['Rel'] == 'moves', char["Links"]))[0]['Href']})

char_list = []
reg = re.compile(r'[@_!#$%^&*()<>,?/\|}{~:]')
for char in char_request_data:
    movements = requests.get(char['link']).json()
    attacks = []
    for move in movements:
        dmg = move['BaseDamage']
        name = move['Name']
        if not reg.search(dmg) and not reg.search(name) and dmg != '':
            if not '-' in dmg:
                if '.' in dmg:
                    dmg = math.ceil(float(dmg))
                else:
                    dmg = int(dmg)
            else:
                dmg = 1
            attacks.append(
                {"damage": dmg, "name": name})

    char.update({'attacks': attacks})
    char.pop('link', None)
    char_list.append(char)

with open('characters.json', 'w') as outfile:
    json.dump(char_list, outfile, indent=2)
