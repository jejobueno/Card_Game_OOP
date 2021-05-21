import random

from typing import List
from utils.card import Card


class Player:
    """
    This class defines each player as object with the following attributes
    -> payer_name: str = The name of the player
    -> cards: List[Card] = The cards of the hand of the player
    -> turn_count: int = This attribute counts the turns played
    -> number_of_cards: int = The quantity of card in attribute cards
    -> history: List[Card] = The historical of the cards played
    :return: Player
    """
    def __init__(self, player_name):
        self.player_name = player_name
        self.cards: List[Card] = list()
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: List[Card] = list()

    def play(self):
        """
        This method plays a random card from the hand of the player.
        Then actualize the number of cards, the turn and the history list
        :return: Card -> the random card taken from the cards of the player
        """
        if len(self.cards) > 0:
            card_to_play = random.choice(self.cards)
            self.turn_count += 1
            self.number_of_cards -= 1
            self.history.append(card_to_play)
            print(
                f'{self.player_name} in the {self.turn_count}° turn played: {card_to_play.value} {card_to_play.symbol}.')
            return card_to_play
        else:
            return 'No cards left'

    def __str__(self):
        """
        Converts the attributes of the player into a string
        :return: str -> Ex 'Player: Jesus
                        'Cards: ["10 [♣ 'black']", "4 [♣ 'black']", "Q [♣ 'black']", "3 [♦ 'red']"]'
                        'Number of cards: 4'
        """
        return f'Player: {self.player_name}\n ' \
               f'Cards: {str([str(card) for card in self.cards])} \n' \
               f'Number of Cards: {self.number_of_cards}'
