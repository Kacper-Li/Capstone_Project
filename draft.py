# 4 main aspects
# - pegging
# - hand
# - box
# - cut card

# Main functionality:
# - deciding first box (both cut, who gets box)
# - Retaining cut card
# - keeping track of deck
# - giving players deck cards.
# - allowing cards to be selected, hence removing from active hand in pegging.
# - Keep track of hand and box and cut card for scoring afterwards


# main function should keep track of deck, cut card, round, scores and pegging progress.

# player functions need to alternate within rounds to allow player 1 then 2 to play...
# this will probably need to become a class rather than function so that state is persistent

# Current plan -> make dummy beginning game 1 round.


# Make this global just cuz it will be used probably everywhere
from itertools import product
from random import shuffle

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


def main():
    deck = list(product(card_ranks, card_suits))
    shuffle(deck)
    ns = 2
    ss = 15
    for i in range(0, len(deck), 4):
        a = f"{deck[i][0]:{ns}} of {deck[i][1]}s"
        b = f"{deck[i+1][0]:{ns}} of {deck[i+1][1]}s"
        c = f"{deck[i+2][0]:{ns}} of {deck[i+2][1]}s"
        d = f"{deck[i+3][0]:{ns}} of {deck[i+3][1]}s"
        print(f"{a:{ss}}| {b:{ss}}| {c:{ss}}| {d}")
    player_1_score = 0
    player_2_score = 0
    pegging_value = 0
    cut_card = ''


main()
