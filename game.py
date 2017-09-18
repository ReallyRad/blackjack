import random


# TODO cleanup and put classes in a module called game
class Card:
    def __init__(self, suit, value):
        # initializes the card
        self.suit = suit
        self.value = value


class Deck:
    # class variables that describe possible values for suits and values
    suits = ("spade", "heart", "diamond", "club")
    values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self):
        # initializes the Deck by creating one instance of each card and adding them to the deck
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(suit, value))

    def display(self):
        # prints all the cards in the deck and the size of the deck
        for card in self.cards:
            print(card.suit, card.value)
        print(len(self.cards))

    def deal(self, player):
        # removes a random card from the deck and adds it to the hand given as a parameter
        card = random.choice(self.cards)
        print(player.name, "was dealt", card.value, card.suit)
        self.cards.remove(card)
        player.hand.cards.append(card)


class Hand:
    def __init__(self, cards=[]):
        self.cards = cards

    def getvalue(self):
        # returns the value of the hand in a blackjack game
        val = 0
        for card in self.cards:
            if card.value.isdigit():
                val += int(card.value)
            else:
                val += 10
        return val


class Player:
    def __init__(self, hand, chips, name):
        # initializes a player by setting its name, amount of chips, and pot
        self.hand = hand
        self.chips = chips
        self.pot = 0
        self.name = name

    def bet(self, amount):
        # removes the amount set as a parameter from the player's chips and adds them to his pot
        self.chips -= amount
        self.pot += amount
        print("player bets", amount)

    def display_chips(self):
        # displays how many chips the player has
        print("player has", self.chips, "chips")
        
class House:
    def __init__(self, hand):
        #the house elemnts are in fact just the hand (rather than chips or name as a player)
        self.hand = hand
