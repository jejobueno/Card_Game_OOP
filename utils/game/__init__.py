from typing import List

from utils.card import Card, Deck
from utils.player import Player


class Board:
    """
    -> players: attribute that is a list of Player. It will contain all
     the players that are playing.
    -> turn_count: counts the turns with an int.
    -> active_cards: that will contain the last card played by each player.
    -> history_cards: that will contain all the cards played since the start
     of the game, with the exception of active_cards
    """

    def __init__(self, players: List[Player]):
        """
        Create the object Board from a list of players and initializes all
        attirbutes
        :param players: contains a list of Players which is made in main.py
        """
        self.players: List[Player] = players
        self.turn_count: int = 0
        self.active_cards: List[Card] = list()
        self.history_cards: List[Card] = list()

    def start_game(self):
        """
        This method creates, fills and shuffles a new deck. Then distributes
        the cards to the players and starts the game calling the method play()
        from each player during the calculated number of turns(the size of the
        hand of the first player).

        After each turn, adds the active cards to the history_cards
        attribute list print the resume of the game with the actual turn
        number, the active cards, and the quantity of played cards.

        Finally resets the list of active cards to an empty list.

        At the end of the game prints the cards left in the deck.
        :return: None
        """
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()

        deck.distribute(self.players)

        for turn in range(0, self.players[0].number_of_cards):
            for player in self.players:
                self.active_cards.append(player.play())
            self.turn_count += 1
            self.history_cards += self.active_cards

            print(f'######## RESUME OF THE GAME #########\n'
                  f'Turn played #: {self.turn_count}\n'
                  f'The active cards are: {str([str(card) for card in self.active_cards])}\n'
                  f'The number of cards player are: {str(len(self.history_cards))}\n')

            self.active_cards = list()

        print(f'Left in the deck: {deck}')
