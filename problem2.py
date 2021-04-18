"""
A generic game of Blackjack, the player competes against the dealer to collect
cards totaling the most points without going over 21.

class Card represents a playing card by defining the attributes suit and rank.
make_deck function returns a shuffled list of all possible 52 cards in a deck.
main function plays a game of Blackjack according to the basic rules provided. 

@author: Stephen Wright (svw2112)
"""

import random
import time


class Card(object): 
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
              
    def __str__(self):
        return "{}{}".format(self.rank, self.suit)

    def value(self, total):
        self.value = 0
        
        if self.rank in ["J", "Q", "K"]:
            self.value = 10
        elif self.rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            self.value = int(self.rank)
        elif self.rank == "A":
            if total + 11 > 21:
                return total + 1
            else:
                return total + 11
        
        return total + self.value


def make_deck():

    deck = []
    suits = ['♠', '♣', '♦', '♥']
    
    for suit in suits:
        for card in range(2, 10):
            deck.append(Card(str(card), suit))
            
        deck.append(Card('J', suit))
        deck.append(Card('Q', suit))
        deck.append(Card('K', suit))
        deck.append(Card('A', suit))

    random.shuffle(deck)
    return deck


def main():
    
    deck = make_deck()
    player_hand = []

    player_total = 0   
    while True:
        card = deck.pop(0)
        player_hand.append(card)
        print("Player card is {}".format(card))
        player_total = card.value(player_total) 
        print("Player hand is {}".format(player_total))
        time.sleep(1)
        
        if player_total == 21:
            print("\nBlackjack - Player Wins! \n<<<Game Over>>>")
            return 
        
        elif player_total > 21:
            print("\nPlayer Bust - Dealer Wins! \n<<<Game Over>>>")
            return
        
        else:
            hit = input("\nDo you want another card? (Y/N)").lower().strip()
            print()
            while hit not in ['y', 'n']:
                print("Invalid entry.")
                hit = input("\nDo you want another card? (Y/N)").lower().strip()
                print()
            if hit != "y":
                break
    
    dealer_total = 0
    while True:
        card = deck.pop(0)
        print("Dealer card is {}".format(card))
        dealer_total = card.value(dealer_total)
        print("Dealer hand is {}\n".format(dealer_total))
        time.sleep(1)
        
        if dealer_total >= 17:
            if dealer_total == 21:
                print("Blackjack - Dealer Wins! \n<<<Game Over>>>")
                return 
            
            elif dealer_total > 21:
                print("Dealer Bust - Player Wins! \n<<<Game over>>>")
                return             
            
            elif dealer_total == player_total:
                print("Push! \n<<<Game Over>>>")
                return 
            
            elif dealer_total > player_total:
                print("Dealer Wins! \n<<<Game Over>>>")
                return
            else:
                print("Player Wins! \n<<<Game Over>>>")   
                return


if __name__ == "__main__":
    main()
