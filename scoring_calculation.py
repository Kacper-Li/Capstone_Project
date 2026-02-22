from card_utils import Card
from card_utils import card_ranks, card_suits
from card_utils import scoring_types
from card_utils import print_deck
from card_utils import total_cards_value
from card_utils import card_value
from card_utils import hands_init
from run_score_calculator import find_biggest_run
from run_score_calculator import find_hand_run
from pair_score_calculator import find_biggest_pair
from pair_score_calculator import find_all_pairs
import itertools
from itertools import product
from random import shuffle
import random


def pegging_scoring(cards: list[Card]) -> int:
    """Based on the very top card of the pile, calculates total score of card played."""
    score = 0
    total_card_rank = total_cards_value(cards)
    if total_card_rank > 31:
        return -1
    elif total_card_rank == 15:
        print("Fifteen for two ", end='')
        score += 2
    elif total_card_rank == 31:
        print("31 for 2 ", end='')
        score += 2
    # print("Cards sending into run and pair calculations: ")
    # print_deck(cards)
    run = find_biggest_run(cards)
    pair = find_biggest_pair(cards)
    if run != 0:
        print(f"Run of {run} ", end='')
    score += run
    if pair != '0':
        print(pair + ' ', end='')
    score += scoring_types[pair]
    # print(f"Total score of card placed: {score}")
    if score == 0:
        print("No points", end='')
    print()
    return score


def hand_scoring(hand: list[Card], cut_card: Card) -> int:
    """Takes a hand of cards, returns the score value TO ADD."""
    score = 0
    hand_plus1 = hand[:]
    hand_plus1.append(cut_card)
    print_deck(hand)
    print(f"Cut card: {cut_card}")
    fifteens = find_all_fifteens(hand_plus1)
    pairs = find_all_pairs(hand_plus1)
    run = find_hand_run(hand_plus1)
    flush = find_hand_flush(hand, cut_card)
    jack = find_jack(hand, cut_card)

    score += scoring_types[flush]
    score += sum([scoring_types[fifteen] for fifteen in fifteens])
    score += scoring_types[jack]
    score += run
    score += sum([scoring_types[pair] for pair in pairs])

    if fifteens:
        print(fifteens, ", ", end='')
    if pairs:
        print(pairs, ", ", end='')
    print(f"Run of {run}, ", end='')
    if flush:
        print(f"Flush: {flush}, ", end='')
    if jack:
        print(f"Jack: {jack} ", end='')

    # print(f"Total score of card placed: {score}")
    if score == 0:
        print("No points", end='')
    print()
    return score


def box_scoring(box: list[Card], cut_card: Card) -> int:
    """Takes a box of cards, returns the score value TO ADD."""
    score = 0
    box_plus1 = box[:]
    box_plus1.append(cut_card)

    print_deck(box)
    print(f"Cut card: {cut_card}")
    # print(box_plus1)
    fifteens = find_all_fifteens(box_plus1)
    pairs = find_all_pairs(box_plus1)
    run = find_hand_run(box_plus1)
    flush = find_box_flush(box_plus1)
    jack = find_jack(box, cut_card)

    score += scoring_types[flush]
    score += sum([scoring_types[fifteen] for fifteen in fifteens])
    score += scoring_types[jack]
    score += run
    score += sum([scoring_types[pair] for pair in pairs])

    if fifteens:
        print(fifteens, ', ', end='')
    if pairs:
        print(pairs, ', ', end='')
    print(f"Run of {run}, ", end='')
    if flush:
        print(f"flush: {flush}, ", end='')
    if jack:
        print(f"Jack: {jack} ", end='')

    # print(f"Total score of card placed: {score}")
    if score == 0:
        print("No points", end='')
    print()
    return score


def find_all_fifteens(cards: list[Card]) -> list[str]:
    raw_cards = [card_value(card) for card in cards]
    # print(raw_cards)
    fifteens = []
    for value in range(len(raw_cards) + 1):
        combination = itertools.combinations(raw_cards, value)
        for combo in combination:
            # print(sum(combo))
            if sum(combo) == 15:
                fifteens.append('15 for two')
    return fifteens


def find_hand_flush(hand: list[Card], cut_card: Card) -> str:
    suit = [card[1] for card in hand]
    if suit.count(suit[1]) == 4:
        if cut_card[1] == suit[1]:
            return 'flush of 5'
        else:
            return 'flush of 4'
    else:
        return '0'


def find_box_flush(box: list[Card]) -> str:
    """Checks for a flush in box, can only be 5 or none."""
    suit = [card[1] for card in box]
    if suit.count(suit[1]) == 5:
        return 'flush of 5'
    else:
        return '0'


def find_jack(cards: list[Card], cut_card: Card) -> str:
    """Returns '1 for his nobs' if jack same suit as cut card found. Else 0."""
    for card in cards:
        if card[0] == 'J' and card[1] == cut_card[1]:
            return '1 for his nobs'
    return '0'


def hand_or_box_init():
    """Initialises hand or box: a set of 4 cards and cut card to score."""
    print("Hands init begins.")
    base_deck = list(product(card_ranks, card_suits))
    p1_score, p2_score = 0, 0
    round_deck = base_deck[:]
    shuffle(round_deck)
    p1_hand, p2_hand = [], []
    hands_init(round_deck, p1_hand, p2_hand)
    p1_hand.pop()
    p1_hand.pop()
    p2_hand.pop()
    p2_hand.pop()
    cut_card = random.choice(round_deck)
    print("p1 hand:")
    print_deck(p1_hand)
    print("p2 hand:")
    print_deck(p2_hand)
    print("cut card:")
    print(cut_card)
    # score
    hob = input("Hand or box?: ")
    if hob.lower() == 'box':
        print("Calculating for box!")
        print("Player 1 stats:")
        p1_score = box_scoring(p1_hand, cut_card)
        print("Player 1 stats:")
        p2_score = box_scoring(p2_hand, cut_card)
        print("----------")
    else:
        print("Calculating for hand!")
        print("Player 1 stats:")
        p1_score = hand_scoring(p1_hand, cut_card)
        print("Player 2 stats:")
        p2_score = hand_scoring(p2_hand, cut_card)
        print("----------")
    print(f"Player 1 score: {p1_score}, Player 2 score: {p2_score}")
    print(f"Player 1 hand: ")
    print_deck(p1_hand)
    print(f"Player 2 hand: ")
    print_deck(p2_hand)


pair2 = [('4', 'Heart'), ('4', 'Club'), ('4', 'Diamond'), ('4', 'Spade')]
# Double Pair Royale / Four of a kind (12 points)
pair3 = [('6', 'Heart'), ('6', 'Club'), ('9', 'Diamond'), ('9', 'Spade')]
# Two pairs with a gap (2 points)

run1 = [('3', 'Heart'), ('5', 'Club'), ('4', 'Diamond')]
# Run 3-4-5 out of order (3 points), Total:12
run2 = [('3', 'Club'), ('2', 'Spade'), ('5', 'Diamond'),
        ('4', 'Heart'), ('7', 'Club'), ('6', 'Heart')]
# Run of six completely out of order: 3-2-5-4-7-6 (6 points), Total:27
run3 = [('4', 'Heart'), ('7', 'Club'), ('6', 'Diamond'), ('5', 'Spade')]
# Run of four: 4-5-6-7 (4 points), Total:22

fifteen = [('8', 'Heart'), ('7', 'Club')]
# Fifteen total: 8 + 7 = 15 (2 points)
thirtyone0 = [('10', 'Heart'), ('J', 'Club'),
              ('A', 'Diamond'), ('Q', 'Spade')]
# Total adding to 31 (2 points)

# 15 + 31: 8 + 7 = 15, total is 31 (4 points)
pairwith15 = [('7', 'Heart'), ('4', 'Club'), ('4', 'Diamond')]
# Pair + 15: pair of 4s (2 points), 11 + 4 = 15 (2 points)

# Tests:
# pegging_scoring(run1)
# pegging_scoring(run2)
# pegging_scoring(pairwith15)
# pegging_scoring(pair2)
# pegging_scoring(pair3)
# pegging_scoring(run3)
# pegging_scoring(fifteen)
# pegging_scoring(thirtyonewith15)

# Tests generated from game
# test1 = []
# test2 = []
# hand1 = [('5', 'Diamond'), ('10', 'Heart'), ('J', 'Heart'), ('Q', 'Heart')]
# hand2 = [('5', 'Club'), ('5', 'Heart'), ('5', 'Diamond'), ('J', 'Spade')]
# hand3 = [('7', 'Club'), ('7', 'Heart'), ('4', 'Diamond'), ('4', 'Heart')]
# hand4 = [('5', 'Club'), ('3', 'Club'), ('2', 'Club'), ('9', 'Club')]
# hand5 = [('7', 'Club'), ('8', 'Spade'), ('9', 'Diamond'), ('7', 'Heart')]
# testing_tries = [hand1, hand2, hand3, hand4, hand5]
# for test in testing_tries:
#     x = box_scoring(test, ('8', 'Club'))
#     print(x)
# pegging_scoring(test3)

# RANDOMISED TESTING
# hand_or_box_init()
