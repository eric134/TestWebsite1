class Deck():
    def __init__(self):
        self.currentDeck = self.newDeck()

    def newDeck(isShuffled):
        suits = ['c', 'd', 'h', 's']
        ranks = ['a', '2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k']
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(f"{rank}{suit}")
        return deck
    
myDeck = Deck()

print(myDeck.currentDeck)
        