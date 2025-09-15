import random

class Deck():
    def __init__(self):
        self.currentDeck = self.createNewUnshuffledDeck()
        self.discardPile = [] # stores all cards that were pulled

    # Deck Manipulation Functions #
    def createNewUnshuffledDeck(self): # creates a completly new, unshuffled deck
        suits = ['c', 'd', 'h', 's']
        ranks = ['a', '2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k']
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(f"{rank}{suit}")
        return deck  
    def shuffle(self): # shuffles the deck
        random.shuffle(self.currentDeck)
    def pullTopCard(self): # returns the top card of the deck and transfers the card to the dicard pile list
        card = self.currentDeck[0]
        self.currentDeck.pop(0)
        self.discardPile.append(card)
        return card
    
        