from game import *
#we start by creating our two players, the player and the house
player = Player(Hand([]), 80, "John")

# TODO make the house a different class instead of another player
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
    bet = int(input("how much do you want to bet?"))
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

