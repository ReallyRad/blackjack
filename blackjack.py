from game import *
# we start by creating our two players, the player and the house
player = Player(Hand([]), 80, "John")
house = Player(Hand([]), 9999999999, "House")

while True:  # loop that allows us to play several times
    # reset the deck
    deck = Deck()

    # reset both player's and house's hands
    player.hand = Hand([])
    house.hand = Hand([])

    # deal one card from the deck to the player's hand
    deck.deal(player)

    # after seeing his card, the player makes a bet
    while True:
        try:
            bet = int(input("how much do you want to bet?"))
        except:
            print("Please type in a number")
        else:
            break

    player.bet(bet)


    deck.deal(player)
    print("your hand is worth", player.hand.getvalue())

    while True:
        if player.hand.getvalue() >= 21:
            break
        answer = input("do you want another card?")

        if answer == "y":
            deck.deal(player)
        elif answer == "n":
            break
        else:
            print("Please type y or n")

    while player.hand.getvalue() <= 21: # loop where the house draws new cards to match the player's
        deck.deal(house)
        if house.hand.getvalue() > player.hand.getvalue() and house.hand.getvalue()>=17:
            break
    print ("house hand is worth", house.hand.getvalue())

    if player.hand.getvalue() > 21:
        print("player went over 21. house wins\n")
        player.pot = 0

    elif player.hand.getvalue() > house.hand.getvalue():
        print("player beats the house\n")
        player.chips += 2*player.pot
        player.pot = 0

    elif house.hand.getvalue() <= 21:
        print("house beats the player\n")
        player.pot = 0

    else:
        print("house went over 21. player wins\n")
        player.chips += 2*player.pot
        player.pot = 0

    player.display_chips()
