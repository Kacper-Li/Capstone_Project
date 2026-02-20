# 4 main aspects
# - pegging
# - hand
# - box
# - cut card

# Main functionality:
# - deciding first box (both cut, who gets box)
# - giving players 6 deck cards alternatively.
# - player without box cuts for cut card
# - allowing cards to be selected, hence removing from active hand in pegging.
# - Keep track of hand and box and cut card for scoring afterwards

# Responsibility:
# main function should track score
# each round resets deck, hands, box and cut card
# main calls --> round till someone wins
# round changes the round deck (giving players cards, cut card)
# pegging happens in round -> round tracks live score.
#

# ORDER MATTERS:
# GAME START = MAKE DECK FRESH
# SHUFFLE DECK
# GIVE EACH PLAYER 6 RANDOM CARDS, ALTERNATE, DELETE FROM GAME_DECK
# THEN CUT CARD, UPDATE+LOG+DELETE(deck will not update anymore so this doesnt strictly matter)


# player functions need to alternate within rounds to allow player 1 then 2 to play...
# this will probably need to become a class rather than function so that state is persistent


# Current plan -> make dummy beginning game 1 round.


# Make this global just cuz it will be used probably everywhere
from itertools import product
from random import shuffle
import random


Card = tuple[str, str]

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


def print_deck(deck: list[Card]) -> None:
    """Takes any list of cards and prints them out in 4 structured columns"""
    ns = 2
    ss = 14
    # print("Printing...")
    for i in range(0, len(deck), 4):
        formatted_parts = []
        for card in deck[i:i+4]:
            card_string = f"{card[0]:{ns}} of {card[1]}s"
            formatted_parts.append(f"{card_string:{ss}}")
        line = ' | '.join(formatted_parts)
        print(line)
    # print("DONE")


# General function to get a card out of any set of cards (hand, box or deck!)
# Needs to be changed to allow a choice rather than random.


def pick_a_card(card_set: list[Card], index=0) -> Card:
    """
    Remove and return a random (rank, suit) card from any card_set.\n
    Manipulates the list of cards directly.
    """
    pick_a_card = card_set.pop(random.randint(0, len(card_set) - 1))
    # print(f"The card chosen at random: {pick_a_card[0]} of {pick_a_card[1]}s")
    return pick_a_card


def hands_init(
    round_deck: list[Card],
    player_1_hand: list[Card],
    player_2_hand: list[Card]
) -> None:
    """Initialises hands, 6 cards each, from the deck. \n
    Manipulated the lists directly."""
    for _ in range(6):
        player_1_hand.append(pick_a_card(round_deck))
        player_2_hand.append(pick_a_card(round_deck))

    # print("Player 1 Hand:")
    # print_deck(player_1_hand)
    # print("Player 2 Hand:")
    # print_deck(player_2_hand)


def box_init(
    player_1_hand: list[Card],
    player_2_hand: list[Card]
) -> list[Card]:
    """Generates and returns the box from the two players hands. \n
    Modifies the hand lists directly"""
    box = []
    box.append(pick_a_card(player_1_hand))
    box.append(pick_a_card(player_1_hand))
    box.append(pick_a_card(player_2_hand))
    box.append(pick_a_card(player_2_hand))
    print("Box: ")
    print_deck(box)
    return box


def pegging_stage(
    pegging_pile: list[Card],
    p1_hand: list[Card],
    p2_hand: list[Card]
) -> tuple[int, int]:
    print("NOT MADE YET")


def calculate_score(*args) -> int:
    print("NOT MADE YET")

# Shuffle deck DONE
# Manipulate deck DONE
# Create Hands (active/ base) DONE
# Create box DONE
# Get cut card DONE
# Pegging pipeline <--


def round(base_deck: list[Card]) -> tuple[int, int]:
    """The main linking of functions, and game flow, to allow the overall game to be played."""
    round_deck = base_deck[:]
    shuffle(round_deck)

    player_1_hand, player_2_hand = [], []
    hands_init(round_deck, player_1_hand, player_2_hand)
    player_1_hand_base = player_1_hand[:]
    player_2_hand_base = player_2_hand[:]

    box = box_init(player_1_hand, player_2_hand)

    # print("Player 1 Hand:")
    # print_deck(player_1_hand)
    # print("Player 2 Hand:")
    # print_deck(player_2_hand)

    print("Round deck:")
    print_deck(round_deck)
    cut_card = pick_a_card(round_deck)
    print_deck([cut_card])

    pegging_pile = []
    pegging_stage(pegging_pile, player_1_hand, player_2_hand)

    calculate_score(player_1_hand_base, cut_card)
    calculate_score(player_2_hand_base, cut_card)
    calculate_score(box, cut_card)


def main():
    base_deck = list(product(card_ranks, card_suits))
    player_1_score = 0
    player_2_score = 0
    # print("Base deck:")
    # print_deck(base_deck)
    round(base_deck)
    # print("Base deck after round:")
    # print_deck(base_deck)


if __name__ == "__main__":
    main()
