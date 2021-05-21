
# Card Game OOP

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)

Development project of cards game for WeTakeYourMoney casino. All players play cards until the don't have any card left :)

![Card game!](https://media.giphy.com/media/3o7TKP35NXE4rWwXjW/giphy.gif)

## How do i play?

First of all you have to run the `main.py` and the game starts on the console! 

This will ask you for a number of players! which should be exactly a number between 1 and 9.
```
♥ ♦ ♣ ♠ Welcome to the play-card game! ♥ ♦ ♣ ♠ 

How many players do you are? Only between 1 and 9 player!: 3
```

Let's say that I want 3 players, so the game is going to ask me for the name of each PLayer (It can'b be the same as another player! If you both have the same name use your lastname, it is going to avoid confusions!: 
```
Ok! 3 player(s)!

Please enter the name of player number 1: Jesus
Welcome Jesus!
```

After each turn, it will print a resume of the game that looks like:
```
######## RESUME OF THE GAME #########
Turn played #: int
The active cards are: List[Card]
The number of cards player are: int
```

The game is over when all the players play all their cards


- ## How does the game really works?
This code will control the input from the command line asking first for a number of player between 1 and 9 and t hen the name of each player which should be and single word creating a list of player. This list is passed to the `Board` object and the game starts calling its `strat_game()` method.

- ## The structure of this projec

```bash
challengeCardGameBecode
│
└───utils
│   └──card.py
│   └──game.py
│   └──player.py
└───main.py
```
