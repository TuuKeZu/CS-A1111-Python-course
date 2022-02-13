# Y1 AUTUMN 2021
# Basic Course in Programming Y1
# Author: Vilma Kahri
# Template for exercise 10.2 Poker

import random

STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIRS = 2
PAIR = 1
HIGH = 0

RESULTSTRINGS = ["high card", "a pair", "two pairs", 
                 "three of a kind", "straight", "flush", 
                 "full house", "four of a kind", "straight flush"]

SPADE = "\u2660"
HEART = "\u2661"
DIAMOND = "\u2662"
CLUB = "\u2663"

SUITS = [SPADE,HEART,DIAMOND,CLUB]
FACES = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
FACES_AS_VALUES = {"2":2, "3":3, "4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}

def initialize_random():
    seed = int(input("Enter a seed number for the random number generator:\n"))
    random.seed(seed)  

def initialize_deck():
    deck = []
    for face in FACES:
        for suit in SUITS:
            card = [face,suit]
            deck.append(card)
    return deck

def shuffle_and_deal(deck):
    random.shuffle(deck)
    player_hand = []
    computer_hand = []
    for i in range(5):
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())
    return deck, player_hand, computer_hand

def check_line(line):
    """
    Parameter: string
    Return value: list of integers
    
    Checks given line that has numbers divided by commas.
    Adds numbers from 1-5 with no duplicates to list.
    """

def draw_more(deck, hand, line):
    """
    Parameters: two-dimensional list, two-dimensional list, string
    Return values: two-dimensional list, two-dimensional list
    
    Deals more cards to hand, cards to change (1-5) 
    are given in string 'line'. (Parses line first using the 
    function check_line.)
    """

def print_hand(hand):
    """
    Parameter: two-dimensional list
    
    Prints the hand that is given as a parameter
    """

def has_straight_flush(hand):
    """
    Parameter: two-dimensional list
    Return values: True, integer or False, None
    
    Checks whether the hand has a straight flush.
    Returns a truth-value accordingly, and the rank card
    value if it did.
    """
    
def has_four_of_a_kind(hand):
    temp = []
    for card in hand:
        temp.append(card[0])
    for face in FACES:
        if temp.count(face) == 4:
            return True, FACES_AS_VALUES[face]
    return False, None

def has_full_house(hand):
    res1, high1 = has_pair(hand) 
    res2, high2 = has_three_of_a_kind(hand)
    if res1 and res2:
        return True, high2
    return False, None

def has_flush(hand):
    """
    Parameter: two-dimensional list
    Return values: True, integer or False, None
    
    Checks whether the hand has a flush.
    Returns a truth-value accordingly, and the rank card
    value if it did.
    """

def has_straight(hand):
    """
    Parameter: two-dimensional list
    Return values: True, integer or False, None
    
    Checks whether the hand has a straight.
    Returns a truth-value accordingly, and the rank card
    value if it did.
    """

def has_three_of_a_kind(hand):
    temp = []
    for card in hand:
        temp.append(card[0])
    for face in FACES:
        if temp.count(face) == 3:
            return True, FACES_AS_VALUES[face]
    return False, None

def has_two_pairs(hand):
    """
    Parameter: two-dimensional list
    Return values: True, integer or False, None
    
    Checks whether the hand has two pairs (not 4 of a kind).
    Returns a truth-value accordingly, and the rank card
    value if it did (the higher of the two pairs).
    """

def has_pair(hand):
    temp = []
    for card in hand:
        temp.append(card[0])
    for face in FACES:
        if temp.count(face) == 2:
            return True, FACES_AS_VALUES[face]
    return False, None

def highest_card(hand):
    """
    Parameter: two-dimensional list
    Return value: integer
    
    Returns the highest card in the hand. 
    """
    
def check_hand(hand):
    """
    Parameter: two-dimensional list
    Return values: Constant and integer
    
    Checks the hand for combinations.
    Returns the constant representing the 
    combination found and the rank card value.
    """

def main():
    initialize_random()
    deck = initialize_deck()
    print("Shuffling and dealing...")
    deck, player_hand, computer_hand = shuffle_and_deal(deck)
    #print(player_hand)
    #print(computer_hand)    # to help perceive the data structures.
    print("Press enter to see your hand.")
    input()
    
    # Continue implementing your code here: 

main()



