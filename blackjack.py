import random

class Card:
    def __init__(self, suit, value):
        #initializes the card
        self.suit = suit
        self.value = value

class Deck:
    #class variables that describe possible values for suits and values
    suits = ("spade","heart","diamond","club")
    values = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

    def __init__(self):
        #initializes the Deck by creating one instance of each card and adding them to the deck
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(suit,value))

    def display(self):
        #prints all the cards in the deck and the size of the deck
        for card in self.cards:
            print(card.suit, card.value)
        print(len(self.cards))

    def deal(self, player):
        #removes a random card from the deck and adds it to the hand given as a parameter
        card = random.choice(self.cards)
        print(player.name, "was dealt", card.value, card.suit)
        self.cards.remove(card)
        player.hand.cards.append(card)

class Hand:
    def __init__(self, cards = []):
        self.cards = cards

    def getValue(self):
        #returns the value of the hand in a blackjack game
        val = 0
        for card in self.cards:
            if card.value.isdigit():
                val += int(card.value)
            else:
                val += 10
        return val

class Player:
    def __init__(self, hand, chips, name):
        #initializes a player by setting its name, amount of chips, and pot
        self.hand = hand
        self.chips = chips
        self.pot = 0
        self.name = name

    def bet(self, amount):
        #removes the amount set as a parameter from the player's chips and adds them to his pot
        self.chips -= amount
        self.pot += amount
        print("player bets", amount)

    def display_chips(self):
        #displays how many chips the player has
        print("player has", self.chips, "chips")

#we start by creating our two players, the player and the house
player = Player(Hand([]), 80, "John")
house = Player(Hand([]), 9999999999, "House")

while True: #loop that allows us to play several times
    #reset the deck
    deck = Deck()

    #reset both player's and house's hands
    player.hand = Hand([])
    house.hand = Hand([])

    #deal one card from the deck to the player's hand
    deck.deal(player)

    #after seeing his card, the player makes a bet
    while True:
        try:
            bet = int(input("how much do you want to bet?"))
        except:
            print("Please type in a number")
        else:
            break
    #TODO add exception handling in the case no number is entered
    player.bet(bet)

    while True: #loop where the player draws new cards
        deck.deal(player)
        if player.hand.getValue() >= 21:
            break

        print("your hand is worth", player.hand.getValue())
        answer = input("do you want another card?")

        if answer == "y":
            pass
        elif answer == "n":
            break

    while player.hand.getValue() <= 21: #loop where the house draws new cards to match the player's
        deck.deal(house)
        if house.hand.getValue() > player.hand.getValue() and house.hand.getValue()>=17:
            break
    print ("house hand is worth", house.hand.getValue())

    if player.hand.getValue() > 21:
        print("player went over 21. house wins\n")
        player.pot = 0

    elif player.hand.getValue() > house.hand.getValue():
        print("player beats the house\n")
        player.chips += 2*player.pot
        player.pot = 0

    elif house.hand.getValue() <= 21:
        print("house beats the player\n")
        player.pot = 0

    else:
        print("house went over 21. player wins\n")
        player.chips += 2*player.pot
        player.pot = 0

    player.display_chips()

