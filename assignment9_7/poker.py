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

def check_line(line = str):
    """
    Parameter: string
    Return value: list of integers
    
    Checks given line that has numbers divided by commas.
    Adds numbers from 1-5 with no duplicates to list.
    """
    result = []

    if(line == ""):
        return []

    data = str(line).split(",")
    
    for char in data:
        num = int(char)

        if(num >= 1 and num <= 5):
            if(num not in result):
                result.append(num)

    return result


def draw_more(deck, hand, line):
    """
    Parameters: two-dimensional list, two-dimensional list, string
    Return values: two-dimensional list, two-dimensional list
    
    Deals more cards to hand, cards to change (1-5) 
    are given in string 'line'. (Parses line first using the 
    function check_line.)
    """
    switched = check_line(line)
    for i in switched:
        hand[i - 1] = deck.pop()

    return deck, hand


def print_hand(hand):
    """
    Parameter: two-dimensional list
    
    Prints the hand that is given as a parameter
    """
    result = ""

    for card in hand:
        result += f"{card[0]}{card[1]} "

    print(result)

def has_straight_flush(hand):
    """
    Parameter: two-dimensional list
    Return values: True, integer or False, None
    
    Checks whether the hand has a straight flush.
    Returns a truth-value accordingly, and the rank card
    value if it did.
    """
    if(has_flush(hand)[0] and has_straight(hand)[0]):
        return True, highest_card(hand)
    else:
        return False, None

    
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
    color = hand[0][1]

    for card in hand:
        if(card[1] != color):
            return False, None

    return True, highest_card(hand)

def has_straight(hand):
    """
    Parameter: two-dimensional list
    Return values: True, integer or False, None
    
    Checks whether the hand has a straight.
    Returns a truth-value accordingly, and the rank card
    value if it did.
    """

    card_numbers = []

    for card in hand:
    
        num = FACES_AS_VALUES[card[0]]

        if(num not in card_numbers):
            card_numbers.append(num)
    # if there are dublicates of numbers => palauttaa False
    if(len(card_numbers) != 5):
        return False, None

    # sort the card numbers
    card_numbers.sort()
    last_num = None

    for i in range(len(card_numbers)):
        num = card_numbers[i]

        if(i == 0):
            last_num = num
        else:
            if(num == (last_num + 1)):
                last_num = num
            else:
                return False, None

    return True, highest_card(hand)

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
    temp = []
    dublicates = []

    for card in hand:
        value = FACES_AS_VALUES[card[0]]
        if(value not in temp and value not in dublicates):
            temp.append(value)
        else:
            if(value not in dublicates):
                dublicates.append(value)

    if(len(dublicates) == 2):
        # Find the highest pair
        highest = 0
        
        for value in temp:
            if(value in dublicates):
                if(value > highest):
                    highest = value
                
                while value in dublicates: dublicates.remove(value)

        return True, highest
    else:
        return False, None


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
    best_card = 0

    for card in hand:
        if(FACES_AS_VALUES[card[0]] > best_card):
            best_card = FACES_AS_VALUES[card[0]]

    return best_card
    
def check_hand(hand):
    """
    Parameter: two-dimensional list
    Return values: Constant and integer
    
    Checks the hand for combinations.
    Returns the constant representing the 
    combination found and the rank card value.
    """
    # DEBUG = [has_straight_flush(hand), has_four_of_a_kind(hand), has_full_house(hand), has_flush(hand), has_straight(hand), has_three_of_a_kind(hand), has_two_pairs(hand), has_pair(hand)]
    # print(DEBUG);

    if(has_straight_flush(hand)[0]):
        return STRAIGHT_FLUSH, has_straight_flush(hand)[1]
    elif(has_four_of_a_kind(hand)[0]):
        return FOUR_OF_A_KIND, has_four_of_a_kind(hand)[1]
    elif(has_full_house(hand)[0]):
        return FULL_HOUSE, has_full_house(hand)[1]
    elif(has_flush(hand)[0]):
        return FLUSH, has_flush(hand)[1]
    elif(has_straight(hand)[0]):
        return STRAIGHT, has_straight(hand)[1]
    elif(has_three_of_a_kind(hand)[0]):
        return THREE_OF_A_KIND, has_three_of_a_kind(hand)[1]
    elif(has_two_pairs(hand)[0]):
        return TWO_PAIRS, has_two_pairs(hand)[1]
    elif(has_pair(hand)[0]):
        return PAIR, has_pair(hand)[1]
    else:
        return HIGH, highest_card(hand)

def main():
    initialize_random()
    deck = initialize_deck()
    print("Shuffling and dealing...")
    deck, player_hand, computer_hand = shuffle_and_deal(deck)
    #print(player_hand)
    #print(computer_hand)    # to help perceive the data structures.
    print("Press enter to see your hand.")
    input()
    
    print("Your hand:")
    print_hand(player_hand)
    p_hand_name, p_highest = check_hand(player_hand)
    print(f"You have {RESULTSTRINGS[p_hand_name]}, rank card value {p_highest}")

    line = input("Enter the cards (1-5) you want to change, separated by commas:\n")
    draw_more(deck, player_hand, line)
    print("Your hand:")
    print_hand(player_hand)
    p_hand_name, p_highest = check_hand(player_hand)
    print(f"You have {RESULTSTRINGS[p_hand_name]}, rank card value {p_highest}")

    print("Press enter to reveal the computer's hand")
    input()

    print("Computer hand:")
    print_hand(computer_hand)
    c_hand_name, c_highest = check_hand(computer_hand)
    print(f"Computer has {RESULTSTRINGS[c_hand_name]}, rank card value {c_highest}")

    # determine the winner
    if(p_hand_name > c_hand_name):
        print("You won.")
    elif(p_hand_name < c_hand_name):
        print("Computer won.")
    elif(p_hand_name == c_hand_name):
        if(p_highest > c_highest):
            print("You won.")
        elif(p_highest < c_highest):
            print("Computer won.")
        elif(p_highest == c_highest):
            print("It's a tie.")

main()



