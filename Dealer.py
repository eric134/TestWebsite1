class Dealer:
    def __init__(self):
        self.dealerSum = 0
        self.playerSum = 0
        self.playerHand = []
        self.dealerHand = []
        self.Deck = []
        self.userChoice = ""

    def dealCards(self):
        self.playerHand.append(deckFunction)
        self.playerHand.append(deckFunction)

        self.dealerHand.append(deckFunction)
        self.dealerHand.append(deckFunction)

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
            self.playerHand.append(insert_deck_function)
            self.checkSum()


        elif self.userChoice.lower() == "stand":
            pass

