import random

suits = [ "Hearts", "Diamonds", "Spades", "Clubs" ]
values = {  "Two": 2, 
            "Three": 3, 
            "Four": 4, 
            "Five": 5, 
            "Six": 6, 
            "Seven": 7, 
            "Eight": 8, 
            "Nine": 9, 
            "Ten": 10, 
            "Jack": 10, 
            "Queen": 10, 
            "King": 10, 
            "Ace": 11 
        }

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return self.value + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()
    
class Player:
    def __init__(self):
        self.hand = []
        self.handValue = 0
        self.ace = 0

    def addCard(self, card):
        self.card = card
        self.hand.append(self.card)
        return self.scoreboard()

    def scoreboard(self):
        self.handValue += values[self.card.value]
        if "Ace" in str(self.card):
            self.ace += 1

        if self.handValue > 21 and self.ace > 0:
            self.handValue -= 10
            self.ace -= 1

        return self.handValue


    #needs dealt card
    #hit vs stay logic
    
class Moola:
    def __init__(self, bet):
        self.amount = 35000
        self.bet = bet

    def addMoola(self):
        return self.amount + self.bet
    
    def subtractMoola(self):
        return self.amount - self.bet


#GAME LOGIC GOES HERE. You could use a class, but lets work out the logic first. 

#ourDeck = Deck()
#ourDeck.shuffleDeck()
#ourCard = ourDeck.dealCard()
#us = Player()
#print(us.addCard(ourCard))
#ourCard = ourDeck.dealCard()
#print(us.addCard(ourCard))
#ourCard = ourDeck.dealCard()
#print(us.addCard(ourCard))
#ourCard = ourDeck.dealCard()
#ourCard = ourDeck.dealCard()
#ourCard = ourDeck.dealCard()
#ourCard = ourDeck.dealCard()
#print(us.addCard(ourCard))
#print(us.addCard(ourCard))
#print(us.addCard(ourCard))
#print(us.addCard(ourCard))
bank = Moola(5500)

print(bank.subtractMoola())


