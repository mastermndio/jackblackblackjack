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
    def __init__(self, amount = 35000):
        self.amount = amount

    def addMoola(self, bet):
        self.bet = bet
        self.amount += self.bet
    
    def subtractMoola(self, bet):
        self.bet = bet
        self.amount -= self.bet

#GAME LOGIC GOES HERE. You could use a class, but lets work out the logic first. 
def gameIntro():
    playGame = input("Hello sirs and or madames, Im Jack Black, the famous actor. I am also a world class Black Jack dealer. Do you want to play a game?(Enter 'yes' to play): ").lower()
    if playGame == "yes":
        return True

    print("Enter 'yes' to play")
    return False


#THE MAIN GAME
def jackblacksblackjack():
    if gameIntro():
        print("Starting Game!")
    else:
        return print("You're boring, you didnt want to play")

    playerMoney = Moola()

    while playerMoney.amount > 0 and playerMoney.amount <= 100000:
        print("Place your bet, you currently have $" + str(playerMoney.amount))

        #Make sure only positive integers and make sure bet is not larger than bank amount
        playerBet = int(input("What is your bet?: "))
        if playerBet > playerMoney.amount and playerBet >= 0:
            print(f"Cant bet more that {playerMoney.amount} and has to be greater than 0")
            continue

        deck = Deck()
        deck.shuffleDeck()

        playerHand = Player()
        dealerHand = Player()

        playerHand.addCard(deck.dealCard())
        dealerHand.addCard(deck.dealCard())
        playerHand.addCard(deck.dealCard())
        dealerHand.addCard(deck.dealCard())
        
        print(f"The Dealer has a {dealerHand.hand[0]} showing")
        
        if dealerHand.handValue == 21:
            print("Jack Black has BLACKJACK!!!!")
            playerMoney.subtractMoola(playerBet)
            continue

        if playerHand.handValue == 21:
            print("Player Wins, BLACKJACK!!!!")
            playerMoney.addMoola(playerBet)
            continue

        while True:
            if playerHand.handValue == 21:
                print("Player Wins, BLACKJACK!!!!")
                playerMoney.addMoola(playerBet)
                break

            print("Your have the following cards")
            for card in playerHand.hand:
                print(card)

            print(f"You have a {playerHand.handValue}")
            hitStay = input("Would you like to [h]it or [s]tay?: ")
        
            if hitStay == 'h':
                playerHand.addCard(deck.dealCard())
                print(f"you were dealt a {playerHand.hand[-1]}")

                if playerHand.handValue > 21:
                    print(f"Your score is {playerHand.handValue}")
                    print("You Lose Loser")
                    playerMoney.subtractMoola(playerBet)
                    break
                continue
            else:
                break


        if playerHand.handValue < 21:
            while True:
                print(f"Dealer hand is {dealerHand.hand}")
                print(f"Dealer score is {dealerHand.handValue}")

                if dealerHand.handValue == 21:
                    print("Jack Black has BlackJack")
                    playerMoney.subtractMoola(playerBet)
                    break

                while dealerHand.handValue < playerHand.handValue:

                    if dealerHand.handValue < 16:
                        dealerHand.addCard(deck.dealCard())
                        print(f"Dealer was dealt a {dealerHand.hand[-1]}")

                        if dealerHand.handValue > 21:
                            print(f"Dealer score is {dealerHand.handValue}")
                            print("You Win, Dealer Sucks!")
                            playerMoney.addMoola(playerBet)
                            break
                        continue
                    else:
                        print("Player wins")
                        playerMoney.addMoola(playerBet)
                        break

                if dealerHand.handValue == 21:
                    print("Jack Black has BlackJack")
                    playerMoney.subtractMoola(playerBet)
                    break

                if dealerHand.handValue > playerHand.handValue and dealerHand.handValue <= 21:
                    print("Dealers wins")
                    playerMoney.subtractMoola(playerBet)
                    break
                break
        


jackblacksblackjack()
