class Blackjack:
    def __init__(self, money):
        self.startSum = money

game = Blackjack(100)

print(game.startSum)