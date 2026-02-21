from itertools import product
from random import shuffle
import random
from card_utils import pick_a_card
from card_utils import hands_init
from card_utils import print_deck
from card_utils import Card
from card_utils import card_ranks, card_suits, scoring_types
from scoring_calculation import pegging_scoring


# Source - https://stackoverflow.com/a/50548011
# Posted by Tom Roth
# Retrieved 2026-02-20, License - CC BY-SA 4.0
import numpy as np
# x1 = (0, 3)
# x2 = (4, 2)
# tuple(np.add(x1, x2))


def pegging_init():
    """Initialises everything for pegging to be tested."""
    print("Pegging setup begins")
    base_deck = list(product(card_ranks, card_suits))
    p1_score, p2_score = 0, 0
    round_deck = base_deck[:]
    shuffle(round_deck)
    p1_hand, p2_hand = [], []
    hands_init(round_deck, p1_hand, p2_hand)
    print("p1 hand:")
    print_deck(p1_hand)
    print("p2 hand:")
    print_deck(p2_hand)
    # We only have the hands created, all thats needed for pegging

    print("Actual pegging begins")
    p1_score, p2_score = pegging_stage(p1_hand, p2_hand, p1_score, p2_score)
    print(f"Player 1 score: {p1_score}, Player 2 score: {p2_score}")
    print(f"player hands: {p1_hand}, {p2_hand}")


def pegging_stage(
    p1_hand: list[Card],
    p2_hand: list[Card],
    p1_score: int,
    p2_score: int
) -> tuple[int, int]:
    """Runs until both hands run out of cards.\nReturns the scores"""
    card_pile: list[Card] = []

    while p1_hand and p2_hand != []:
        card_pile.append(pick_a_card(p1_hand))
        turn_score = pegging_scoring(card_pile)
        if turn_score == -1:
            card_pile = [card_pile[-1]]
            print("card pile reset---------------------")
            turn_score = 0
            print("Player 2 gets 1 for go")
            p2_score += 1
        print("p1 card pile:", card_pile)
        print(f"Player 1 gets {turn_score}")
        print("Next: ", end='')
        p1_score += turn_score
        card_pile.append(pick_a_card(p2_hand))
        turn_score = pegging_scoring(card_pile)
        if turn_score == -1:
            card_pile = [card_pile[-1]]
            print("card pile reset---------------------")
            turn_score = 0
            print("Player 1 gets 1 for go")
            p1_score += 1
        print("p2 card pile:", card_pile)
        print(f"Player 2 gets {turn_score}")
        print("Next: ", end='')
        p2_score += turn_score

    return p1_score, p2_score


pegging_init()


# SCORING SHOULD ONLY CARE ABOUT THE LAST CARD PLACED,
# IN RELATION TO THE CURRENT CARDS ALREADY PLACED.
# HISTORY OF SCORES OR CONDITIONS DONT MATTER

# I.E. IF THERE WAS OR WASNT A RUN OF 3 DOESNT MATTER
# IF YOU ARE CHECKING FOR A RUN OF 4.

# WHETHER THE FIRST OR SECOND CARD IS SAME SUIT
# DOESNT MATTER FOR A FLUSH CHECK AT 4TH OR 5TH CARD PLACED

# WHETHER THERE WAS ANOTHER PAIR BEFORE YOUR CURRENT PAIR
# DOESNT MATTER BECAUSE YOU CHECK FOR PAIR ROYALE ANYWAY.

# IN CONCLUSION, YOU CALCULATE THE SCORE FROM CURRENT CARD.
# PREVIOUS SCORES ARE IRRELEVANT.
