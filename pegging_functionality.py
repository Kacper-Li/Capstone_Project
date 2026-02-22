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


def pegging_init():
    """Initialises everything for pegging to be tested."""
    print("Pegging setup begins")
    base_deck = list(product(card_ranks, card_suits))
    non_dealer_score, dealer_score = 0, 0
    round_deck = base_deck[:]
    shuffle(round_deck)
    non_dealer_hand, dealer_hand = [], []
    hands_init(round_deck, non_dealer_hand, dealer_hand)
    non_dealer_hand.pop()
    non_dealer_hand.pop()
    dealer_hand.pop()
    dealer_hand.pop()
    # p1h = [('3', 'Spade'), ('3', 'Diamond'), ('2', 'Diamond'), ('A', 'Heart')]
    # p2h = [('9', 'Spade'), ('Q', 'Diamond'), ('K', 'Diamond'), ('10', 'Heart')]
    # non_dealer_hand = p1h
    # dealer_hand = p2h
    print("p1 hand:")
    print_deck(non_dealer_hand)
    print("p2 hand:")
    print_deck(dealer_hand)
    # We only have the hands created, all thats needed for pegging

    print("Actual pegging begins")
    non_dealer_score, dealer_score = pegging_stage(
        non_dealer_hand, dealer_hand, non_dealer_score, dealer_score)
    print(
        f"Player 1 score: {non_dealer_score}, Player 2 score: {dealer_score}")
    print(f"player hands: {non_dealer_hand}, {dealer_hand}")


def pegging_stage(
    non_dealer_hand: list[Card],
    dealer_hand: list[Card],
    non_dealer_score: int,
    dealer_score: int
) -> tuple[int, int]:
    """Runs until both hands run out of cards.\n
    Returns the scores: Non-Dealer, Dealer"""
    card_pile: list[Card] = []
    last = 'E'

    while non_dealer_hand != [] or dealer_hand != []:
        # WANT:
        # if p1 has no valid cards, let p2 go, if p2 has no valid cards
        # reset peg
        placeable_1 = can_place(non_dealer_hand, card_pile)
        if placeable_1:
            card_pile, non_dealer_diff, dealer_diff = player_turn(
                non_dealer_hand, card_pile, "Non-Dealer")
            non_dealer_score += non_dealer_diff
            dealer_score += dealer_diff
            last = '1'

        placeable_2 = can_place(dealer_hand, card_pile)
        if placeable_2:
            card_pile, dealer_diff, non_dealer_diff = player_turn(
                dealer_hand, card_pile, "Dealer")
            dealer_score += dealer_diff
            non_dealer_score += non_dealer_diff
            last = '2'
        if placeable_1 == [] and placeable_2 == []:
            card_pile = []
            if last == '1':
                non_dealer_score += 1
                print(f"Non-Dealer gets one for go!")
            else:
                dealer_score += 1
                print(f"Dealer gets one for go!")
    if last == '1':
        non_dealer_score += 1
        print(f"Non-Dealer gets one for last!")
    else:
        dealer_score += 1
        print(f"Dealer gets one for last!")
    return non_dealer_score, dealer_score


def player_turn(
    hand: list[Card],
    card_pile: list[Card],
    player: str,
) -> tuple[list[Card], int, int]:
    """Lets a player place a card, scores it, returns card pile and score deltas.
    \nHandles pegging reset"""
    other_player_score = 0
    playable_cards = can_place(hand, card_pile)
    # if (playable_cards) != []:
    card_to_play = random.choice(playable_cards)
    card_pile.append(card_to_play)
    hand.remove(card_to_play)
    print("Next: ", end='')
    turn_score = pegging_scoring(card_pile)
    # else:
    #     card_to_play = random.choice(hand)
    #     card_pile = [card_to_play]
    #     hand.remove(card_to_play)
    #     print("card pile reset")
    #     turn_score = 0
    #     print(f"{other_player} gets 1 for go")
    #     other_player_score = 1
    print(f"{player} turn. card pile:", card_pile)
    print(f"{player} gets {turn_score}\n -------------------")
    return card_pile, turn_score, other_player_score


def can_place(hand: list[Card], pile: list[Card]) -> list[Card]:
    """Tests if a hand can possibly place in pegging.\nReturns available cards"""
    total_placed_value = total_cards_value(pile)
    value_remaining = 31 - total_placed_value
    # print(f"Max value allowed: {value_remaining}")
    placeable_cards = []
    for card in hand:
        if card_value(card) <= value_remaining:
            placeable_cards.append(card)
    return placeable_cards


# pegging_init()


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
