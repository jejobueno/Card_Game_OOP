import re

from typing import List

from utils.game import Board
from utils.player import Player

""" This code will control the input from the command line
    asking first for a number of player between 0 and 9 and 
    then the name of each player which should be and single 
    word creating a list of player.
    This list is passed to the board and starts the game
"""

print('♥ ♦ ♣ ♠ Welcome to the play-card game! ♥ ♦ ♣ ♠ \n')
while True:
    quantity_player = input('How many players do you are? Only between 1 and 9 player!: ')
    if re.search(r"^[1-9]$", quantity_player):
        print(f'Ok! {quantity_player} player(s)!\n')
        break
    else:
        print("Please only numbers!. Try again!")

players: List[Player] = list()

for i in range(0, int(quantity_player)):
    while True:
        player = input(f'Please enter the name of player number {i + 1}: ').lower().capitalize()
        if re.search(r"^[a-zA-Z]+$", player):
            if [player.player_name for player in players].__contains__(player):

                print("Player already exist." " Try a new name!\n")
            else:
                print(f'Welcome {player}!\n')
                players.append(Player(player))
                break
        else:
            print("Please only letters and no blank spaces!. Try again!")


board = Board(players)

board.start_game()