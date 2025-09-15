from cardFunctions import *

deck = Deck()


class Dealer:
    def __init__(self):
        self.dealerSum = 0
        self.playerSum = 0
        self.playerHand = []
        self.dealerHand = []
        self.Deck = []
        self.userChoice = ""

    def dealCards(self):
        self.playerHand.append(deck.pullTopCard())
        self.playerHand.append(deck.pullTopCard())

        self.dealerHand.append(deck.pullTopCard())
        self.dealerHand.append(deck.pullTopCard())


    def checkSum(self):
        if self.playerSum > 21:
            print("You have busted!")
        if self.playerSum == 21:
            print("Blackjack!")
        if self.dealerSum > 21:
            print("The dealer has busted!")

    def play(self):
        # User hits
        if self.userChoice.lower() == "hit":
            # Add card to hand
            self.playerHand.append(deck.pullTopCard())
            self.checkSum()


        elif self.userChoice.lower() == "stand":
            pass

dealer = Dealer()
deck.shuffle()
dealer.dealCards()
print(dealer.playerHand)