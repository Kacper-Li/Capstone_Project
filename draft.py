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


def print_deck_52(deck):
    ns = 2
    ss = 14
    print("Printing...")
    for i in range(0, len(deck), 4):
        formatted_parts = []
        for card in deck[i:i+4]:
            card_string = f"{card[0]:{ns}} of {card[1]}s"
            formatted_parts.append(f"{card_string:{ss}}")
        line = ' | '.join(formatted_parts)
        print(line)
    print("DONE")

# Shuffle deck DONE
# Manipulate deck <---
# Create Hands (active/ base)
# Create box
# Get cut card
# Pegging pipeline


def round(base_deck: list[tuple]) -> tuple:
    round_deck = base_deck[:]
    shuffle(round_deck)
    # pick_a_card = round_deck.pop(random.randint(0, len(round_deck) - 1))
    # print("This is the card chosen at random:",
    #       pick_a_card, "\n This is the new deck:")
    print("Round deck:")
    print_deck_52(round_deck)


def main():
    base_deck = list(product(card_ranks, card_suits))
    # print("Base deck:")
    # print_deck_52(base_deck)
    round(base_deck)
    # print("Base deck after round:")
    # print_deck_52(base_deck)

    player_1_score = 0
    player_2_score = 0


main()
