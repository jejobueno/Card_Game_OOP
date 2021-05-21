import random

from typing import List

SYMBOLS: List[chr] = ['♥', '♦', '♣', '♠']
CARD_VALUES: List[chr] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Symbol:
    """
    The object Symbol contain the values of the symbol in a single card
    ('♥', '♦', '♣', '♠').It's attributes are symbol and color. Ex [♥ 'black']
    """
    color: str
    icon: chr

    def __init__(self, icon, color):
        """
        Initializes a Symbol object
        :param icon: str -> one symbol from the list ('♥', '♦', '♣', '♠')
        :param color: str -> can be rather 'black' or 'red'
        """
        self.icon = icon
        self.color = color

    def __str__(self):
        """
        Converts the attributes of the Symbol into a string
        :return: str -> Ex [♥ 'black']
        """
        return f"[{self.icon} '{self.color}']"


class Card:
    def __init__(self, value: chr, symbol: Symbol):
        """
        This method initializes a new object Card
        :param value: str -> from list
        ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        :param symbol: str -> from list ['♥', '♦', '♣', '♠']
        """
        self.value: chr = value
        self.symbol: Symbol = symbol

    def __str__(self):
        """
        Converts the attributes of the player into a string
        :return: str -> Ex ["10 [♣ 'black']
        """
        return self.value + ' ' + str(self.symbol)


# Import placed here to avoid circular import error
from utils.player import Player


class Deck:

    def __init__(self):
        """
        Initializes a new Deck object with a empty list of Cards
        :return: Deck
        """
        self.cards: List[Card] = list()

    def fill_deck(self):
        """
        fill_deck method creates the respective Symbol objects to after
        create the respective 52 Card objects and add them to the `cards`
        attribute from the object Deck.
        :return: None
        """
        symbols = [Symbol(icon, 'red') for icon in SYMBOLS[0:2]]
        symbols += [Symbol(icon, 'black') for icon in SYMBOLS[2:]]

        for value in CARD_VALUES:
            for icon in symbols:
                new_card = Card(value, icon)
                self.cards.append(new_card)

    def shuffle(self):
        """
        This method shuffles randomly the deck
        :return: None
        """
        random.shuffle(self.cards)

    def distribute(self, players: List[Player]):
        """
        This method distribute equally the cards between the players.
        adding each Card to the cards list of each Player and adding the
        number_of_cards of each Player by one
        :param: players: List[PLayer] -> players on the game
        :return: None
        """
        for i in range(int(len(self.cards) / len(players))):
            for player in players:
                player.cards.append(self.cards.pop())
                player.number_of_cards += 1

    def __str__(self):
        """
        Converts the attributes of the Card into a string
        :return: List[Card]
        -> Ex '["10 [♣ 'black']", "4 [♣ 'black']", "Q [♣ 'black']", "3 [♦ 'red']"]'
        """
        return str([str(card) for card in self.cards])
