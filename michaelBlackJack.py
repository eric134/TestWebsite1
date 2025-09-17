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
        self.possibleHitAnswers = ['h', 'hit']
        self.possibleStandAnswers = ['s', 'stand']
        self.playerMoney = 100
        self.playerBet = 0
        self.playerHand = []
        self.dealerHand = []

        self.isNewGame = True
        self.isWaiting = True
        self.isBetting = False
        self.isPlaying = False
        self.isDealing = False
        self.isPlayerTurn = False
        self.isDealerTurn = False
        self.isPlayerOver = False
        self.isDealerOver = False
        self.isPush = False
        self.isPlayerHitting = False
        self.isPlayerStanding = False

    def startBetting(self): # Starts the pre game betting logic
        print(f"You have ${self.playerMoney} to bet with")
        while self.playerBet <= 0 or self.playerBet > self.playerMoney:

            try:
                answer = input("How much would you like to bet?: ")
                self.playerBet = float(answer)

                if self.playerBet <= 0 or self.playerBet > self.playerMoney:
                    print(f"i can't accept your bet of ${self.playerBet}")
                else:
                    break
            except ValueError:
                print(f"I don't think ${str(answer)} is any sort of number")
                pass
        print(f"----------\nYour bet of ${self.playerBet} has been taken\n----------")
        self.isPlaying = True
        self.isBetting = False
    def playing (self):
        
        self.isDealing = True
        while True:
            if len(self.playerHand) < 2:
                self.playerHand.append(deck.pullTopCard())
            if len(self.dealerHand) < 2:
                self.dealerHand.append(deck.pullTopCard())
            print(self.playerHand, self.dealerHand)
            if self.isDealing:
                continue
            
            
            print(f"Dealer Cards: {self.dealerHand[0][0]} + ??\nPlayer Cards: {self.playerHand[0][0]} + {self.playerHand[1][0]}")
            answer = str(input("Hit or Stand?: ")).lower
            if answer in self.possibleHitAnswers:
                pass



# TESTING #

deck = Deck()
game = Game()
game.startBetting()
game.playing()

#         #