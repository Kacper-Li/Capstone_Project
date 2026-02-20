from itertools import product
from random import shuffle
import random
from draft import pick_a_card
from draft import hands_init

card_suits = ['Club', 'Diamond', 'Heart', 'Spade']
card_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
scoring_types = {
    'type': "score_value",
    '15': 2,
    'pair': 2,
    'pair royale': 6,
    'double pair royale': 12,
    'run of 3': 3,
    'run of 4': 4,
    'run of 5': 5,
    'flush of 4': 4,
    'flush of 5': 5,
    'last peg': 1,
    '31': 2,
    '2 for his heels': 2,
    '1 for his nobs': 1,
}


def pegging_init():
    """Initialises everything for pegging to be tested."""
    base_deck = list(product(card_ranks, card_suits))
    p1_score, p2_score = 0, 0
    round_deck = base_deck[:]
    shuffle(round_deck)
    p1_hand, p2_hand = [], []
    hands_init(round_deck, p1_hand, p2_hand)


def pegging_stage1(p1_hand: list[tuple[str, str]], p2_hand: list[tuple[str, str]]) -> tuple[int, int]:
    """Runs until both hands run out of cards.\nReturns the scores"""
    while p1_hand and p2_hand != []:
        print("poo")
