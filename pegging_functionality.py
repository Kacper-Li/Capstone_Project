from itertools import product
from random import shuffle
import random
from card_utils import pick_a_card
from card_utils import hands_init
from card_utils import print_deck
from card_utils import card_value
from card_utils import total_cards_value
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

    while p1_hand or p2_hand != []:

        card_pile, p1_diff, p2_diff = player_turn(
            p1_hand, card_pile, "Player 1")
        p1_score += p1_diff
        p2_score += p2_diff

        card_pile, p2_diff, p1_diff = player_turn(
            p2_hand, card_pile, "Player 2")
        p2_score += p2_diff
        p1_score += p1_diff
    return p1_score, p2_score


def player_turn(
    hand: list[Card],
    card_pile: list[Card],
    player: str,
) -> tuple[list[Card], int, int]:
    """Lets a player place a card, scores it, returns card pile and score deltas."""
    if player == "Player 1":
        other_player = "Player 2"
    else:
        other_player = "Player 1"
    other_player_score = 0
    if (can_place(hand, card_pile) != []):
        card_pile.append(pick_a_card(hand))
        print("Next: ", end='')
        turn_score = pegging_scoring(card_pile)
    else:
        turn_score = -1
    if turn_score == -1:
        card_pile = [card_pile[-1]]
        print("card pile reset---------------------")
        turn_score = 0
        print(f"{other_player} gets 1 for go")
        other_player_score = 1
    print(f"{player} turn. card pile:", card_pile)
    print(f"{player} gets {turn_score}\n -------------------")
    return card_pile, turn_score, other_player_score


def can_place(hand: list[Card], pile: list[Card]) -> Card:
    """Tests if a hand can possibly place in pegging.\nReturns available cards"""
    total_placed_value = total_cards_value(pile)
    value_remaining = 31 - total_placed_value
    placeable_cards = []
    for card in hand:
        if card_value(card) <= value_remaining:
            placeable_cards.append(card)
    return placeable_cards


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
