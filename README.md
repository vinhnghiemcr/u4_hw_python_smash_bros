# Python Smash Brothers

<p>
<img align="left" src="https://38.media.tumblr.com/b2bad3b19677a58ed9ef02e4d0eb0e24/tumblr_nce6ckWyAR1qdripwo1_500.gif" />
<img align="right" src="https://thumbs.gfycat.com/SoftConsciousBlackrussianterrier-size_restricted.gif" />
<img align="right" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia1.tenor.com%2Fimages%2F1610b2265a0c14c45b6011a0f5b95464%2Ftenor.gif%3Fitemid%3D12409005&f=1&nofb=1" />
<img align="left" src="https://www.ssbwiki.com/images/thumb/2/2e/SSB64_Yoshi_Combo.gif/200px-SSB64_Yoshi_Combo.gif" />
<img align="center" src="https://www.ssbwiki.com/images/thumb/a/af/SSB64_Greenhouse_Combo.gif/250px-SSB64_Greenhouse_Combo.gif" />
</p>

## Overview
Have you ever wondered what happens behind the scenes with Smash Brothers? In this lab, we'll be building a simplified version of the game to get practice with Python OOP by building classes for characters and battles! While there are minimum requirements, you're more than welcome to make this as accurate as possible post MVP!

## Getting Started
- `Fork` and `clone` this repository

___
## Instructions
### Data
We'll be working with the data found in `characters.json`. This data should be imported into our `smash.py` file and used to populate instances of our Character class. 

### Classes
We'll be creating two classes in the `smash.py` file with the following specifications:
- Create a Battle and Character class in the `smash.py` file.
- The Character class should have at least a character's name, health, and list of their moves
- It should also be able to decrement character's health and select a random attack from their list of moves
- The Battle class should take in two Characters to start a battle

### Game
In the `main.py` file we'll import our classes and use them within a `game` function. The `game` function should do the following:
- Allow users to select a character from the terminal when the game starts: `input()` may be useful here
- Determine a winner if a Character has health less than zero
- If the user does not select a Character, a random one is chosen for them
- Opponents should be chosen at random

## Requirements

- The battle class should accept two characters to start the battle
- The character class should create a character using a minimum of their name and a list of attacks
- In the character class, you should be able to decrement the characters health and select a random attack from the list.
- The game should run from the `main.py` file.
- Be able to choose a character in the terminal, hint: `input` may be useful.
- Should declare a winner based on who has the highest remaining health.
- If the user does not select a character, a random one should be chosen for them.
- The opponent should be chosen at random, hint: `random.choice` may be useful.

## Bonus
- Try to make a game that allows for restarts after a player wins and keeps track of total score.
- Try to populate your Character class instances with more data, resources for this data have been provided below

___
## Submission Guidelines

Submit your pull request utilizing the **[Pr Guidelines](https://github.com/SEI-R-1-25/template_pull_request)**.

Pull requests are due by next day at `10:00 am EST`.

## Resources
- [Python OOP Lesson](https://github.com/SEI-R-1-25/u4_lesson_python_oop)
- [The KuroganeHammer API Docs](https://api.kuroganehammer.com/swagger/index.html)
  - Base URL: https://api.kuroganehammer.com/api/
- [Python Requests Module](https://2.python-requests.org/en/master/)
