""" In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

And most importantly:

    You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!

Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! Remember to you are free to use any resources you want and as always:
HAVE FUN! """


#GLOBAL VARIABLES AND IMPORT STATEMENTS

import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", 
"King", "Ace")

values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, 
"Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

game_on = True


# CLASS DEFINITIONS

class Card():

    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks

    def __str__(self):
        return (f"{self.ranks} of {self.suits}")


class Deck(Card):

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(f"{rank} of {suit}")

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
        
        

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.split()[0]]
        if (card.split()[0] == "Ace"):
            self.aces += 1

    def adjust_for_ace(self):
        while (self.value > 21 and self.aces):
            self.value -= 10
            self.aces -= 1



class GameTokens():

    def __init__(self):

        self.total = int(input("\nHow many money do you want to change?: "))
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# FUNCTIONS DEFINITIONS

def take_bet(coins):
    while True:
        try:
            bet = int(input("\nWhat is you bet?: "))
            if (bet > coins.total):
                print("\nYou don't have enough money")
            elif (0 < bet <= coins.total):
                coins.bet = bet
                coins.total -= bet
                break
        except:
            print("\nError! Please try again")


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global game_on
    while True:
        if (hand.value < 21):
            ask = str(input("\nDo you want to hit or stand? H - S: "))
            if (ask.upper() == "H"):
                hit(deck,player_hand)
                break
            else:
                print("\nPlayer stands. Dealer is playing")
                game_on = False
                break
        else:
            game_on = False
            break



def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1]) 
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n ')
    print("Player's Hand =",player_hand.value)

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer_hand.cards, sep='\n ')
    print("Dealer's Hand =",dealer_hand.value)
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n ')
    print("Player's Hand =",player_hand.value)

def player_busts(player, dealer, coins):
    print("\nPlayer lose!")
    coins.lose_bet()

def player_wins(player, dealer, coins):
    print("\nPlayer win!")
    coins.win_bet()

def dealer_busts(player, dealer, coins):
    print("\nDealer lose!")
    coins.win_bet()

def dealer_wins(player, dealer, coins):
    print("\nDealer win!")
    coins.lose_bet()

def push(player, dealer, coins):
    print("\nDealer and Player tie! It's a push.")



# GAMEPLAY

ready = True

while ready:

    game_on = True
    
    # Opening statement
    ready = input("\nWelcome to the BlackJack Game!! Get as close to 21 as you can!\n"
    "Dealer hits until reaches 17. Aces count as 1 or 11.\n\nAre you ready to play? Yes - No: ")

    if (ready == "Yes" or ready == "Y" or ready == "yes" or ready == "y"):
        
        # Create and shuffle the deck, deal two cards to each players
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's coins
        coins = GameTokens()
        coins.total
        
        # Prompt the Player for their bet
        take_bet(coins)

        # Show cards (one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while game_on:
            
            # Prompt for Player to hit or stand
            hit_or_stand(deck, player_hand)

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            # Show cards (one dealer card hidden)
            show_some(player_hand, dealer_hand)
            

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if (player_hand.value > 21):

                player_busts(player_hand, dealer_hand, coins)
                break
        
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if (player_hand.value <= 21):

            while (dealer_hand.value < 17):
                hit(deck, dealer_hand)
            
            # Show all cards
            show_all(player_hand, dealer_hand)

            #Run different winning scenarios
            if (dealer_hand.value > 21):
                dealer_busts(player_hand, dealer_hand, coins)
                
            elif (player_hand.value < dealer_hand.value):
                dealer_wins(player_hand, dealer_hand, coins)
                
            elif (dealer_hand.value < player_hand.value):
                player_wins(player_hand, dealer_hand, coins)
                
            else:
                push(player_hand, dealer_hand, coins)
        
        # Inform Player of their chips
        print(f"\nPlayer's winnings stand at: {coins.total}")

        # Ask to play again
        ready = input("\nDo you want to play again? Yes - No: ")        
        if (ready == "Yes" or ready == "Y" or ready == "yes" or ready == "y"):
            ready = True
        else:
            ready = False
            print("\nThanks for playing! See you!!")
            #break

    else:
        ready = False
        break
