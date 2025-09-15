import random

class Deck():
    def __init__(self): 
        self.currentDeck = self.createNewDeck()
        self.discardPile = []
    
    def createNewDeck(self): # initializes a new list of unshuffled "cards". Each card is made up of an ID: a 2 character string

        # The suits and ranks are stored in string fashion
        suits = "cdhs" 
        ranks = "a23456789tjqk"

        # Deck is then generated
        newDeck = []
        for suit in suits:
            for rank in ranks:
                newDeck.append(f"{rank}{suit}")


        return newDeck
    def shuffle(self): # shuffles the deck
        random.shuffle(self.currentDeck)
    def pullTopCard(self): # returns the first card in the list of cards and also appends it to the discard pile list
        pulledCard = self.currentDeck[0]
        self.currentDeck.pop(0)
        self.discardPile.append(pulledCard)
        return pulledCard

class Game():

    def __init__(self):
        self.isBetting = False
        self.isPlaying = False
        self.isPlayerTurn = False
        self.isDealerTurn = False
        self.isPlayerOver = False
        self.isDealerOver = False
        self.isPush = False
        self.isPlayerHitting = False
        self.isPlayerStanding = False

    def startGame(self):
        pass

deck = Deck()
deck.pullTopCard()
print(deck.discardPile)