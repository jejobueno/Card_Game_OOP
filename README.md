
# Card Game OOP

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)

Development project of cards game for WeTakeYourMoney casino. All players play cards until the don't have any card left :)

![Card game!](https://media.giphy.com/media/3o7TKP35NXE4rWwXjW/giphy.gif)

## How do i play?

First of all you have to run the code in the file `main.py` and the game starts on the console! 

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

### Attributes:

   - `possible_words`:
      It contains a list of words. Out of these words, one will be
    selected as the word to find. The list must also contain the following words:
    ['becode', 'learning', 'mathematics', 'sessions'].
   - `word_to_find`: 
      attribute that contains a list of strings. Each element will be a letter of
    the word.
   - `lives`:
   attribute that contains the number of lives that the player still has left. It should
    start at 5.
   - `correctly_guessed_letters`:
   attribute that contains a list of strings where each element will
    be a letter guessed by the user. At the start, it should be equal to: ```['_', '_', '_', '_', '_']```, with the
     same number of '_' as the length of the word to find.
   - `wrongly_guessed_letters`:
    attribute that contains a list of strings where each element will be
   a letter guessed by the user that is not in the word_to_find.
   - `turn_count`:
      attribute that contain the number of turns played by the player. This will be
   represented as an int.
   -`error_count`: attribute that contains the number of errors made by the player.
   
### Methods:

  - `__init__(self, possible_words: List[str])`:
        This method initialize the Hangman object with a list of possbile words
        :param possible_words: contains all possible word that can be chosen
        as word to find. Default value = ["becode", "learning", "mathematics", "sessions"]
  - `game_over(self)`:
       This method will print 'game over...' before breaking the loop
       and finishing the game.
   
  - `play(self)`:
       `play()` method will has to the player for a single letter, if it is not
       a letter it will ask again a new input. If it is a uppercase later it
       transform it in a lowercase letter.
       :self.turn_count: is increased by one each time the player plays
       The method checks if word_to_find contains the letter,
       :if True: it sets the letter in the correspondent indexes in the
       `correctly_guessed_letters` attribute.
      :if False: it sets the letter in the correspondent indexes in the
       `wrongly_guessed_letters` attribute, incrementing the `error_count` and
       decreasing the `lives` attributes by one.
   
  - `start_game(self)`:
       This function will first to choose randomly one of the "possible words" and
       saves it as a list of single chars into `word_to_find` attribute. Then create
       a list of spaces of the same size as `word_to_find`and initialize all the 
       attributes.so that this method can be called as many times as you want to play!.
       Afterwards, it calls the `play()` method letting the user play.
       If the player has no more lives, it calls the `game_over()` method
       If the player has guessed correctly the word, it calls `well_played()` method
       (`correctly_guessed_letters == self.word_to_find`)
   
  - `well_played(self)`:
       This method will print a review of the game after the player guessed
       correctly the word. It prints the guessed word (`word_to_find`), and the
       count of turns and error
 

