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
from card_utils import Card
from card_utils import pick_a_card
from card_utils import print_deck
from card_utils import card_ranks
from card_utils import card_suits
from card_utils import hands_init
from pegging_functionality import pegging_stage
from scoring_calculation import hand_scoring, box_scoring


# General function to get a card out of any set of cards (hand, box or deck!)
# Needs to be changed to allow a choice rather than random.

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

# Shuffle deck DONE
# Manipulate deck DONE
# Create Hands (active/ base) DONE
# Create box DONE
# Get cut card DONE
# Pegging pipeline DONE DONE DONE


def round_functionality(
    base_deck: list[Card],
    p1_score: int,
    p2_score: int,
    round: int
) -> tuple[int, int]:
    """The main linking of functions, and game flow, to allow the overall game to be played.\n
    Returns player scores p1, p2 and controls flow of who gets box, pegging, scoring hand and box."""
    round_deck = base_deck[:]
    shuffle(round_deck)

    player_1_hand, player_2_hand = [], []
    hands_init(round_deck, player_1_hand, player_2_hand)
    player_1_hand_copy = player_1_hand[:]
    player_2_hand_copy = player_2_hand[:]

    box = box_init(player_1_hand, player_2_hand)

    print("Player 1 Hand:")
    print_deck(player_1_hand)
    print("Player 2 Hand:")
    print_deck(player_2_hand)
    separator = "||||||||||||||||||||"
    print("Round deck:")
    print_deck(round_deck)
    cut_card = pick_a_card(round_deck)
    print("Cut card chosen randomly: ", cut_card)
    print(f"{separator} ROUND BEGINS!!!! {separator}")
    if (round % 2) == 1:
        print("Player 1's turn with box!")
        # meaning player 2 places first in pegging
        p2_diff, p1_diff = pegging_stage(
            player_2_hand_copy, player_1_hand_copy, p2_score, p1_score)
        p1_score += p1_diff
        p2_score += p2_diff
        print(f"{separator} Pegging done! Moving on! {separator}")
        print("\nSince player 1 has box, player 2 gets their hand scored first!")
        print("Hand:")
        p2_diff = hand_scoring(player_2_hand, cut_card)
        p2_score += p2_diff
        print(f"Points earned: {p2_diff}")
        print("\nNow player 1 gets their hand and then box scored!")
        print("Hand:")
        p1_diff = hand_scoring(player_1_hand, cut_card)
        p1_score += p1_diff
        print(f"Points earned: {p1_diff}")
        print("Box:")
        p1_diff = box_scoring(box, cut_card)
        p1_score += p1_diff
        print(f"Points earned: {p1_diff}")
        print(f"{separator} Scoring round completely finished! {separator}")

    else:
        print("Player 2's turn with box!")
        # meaning player 1 places first in pegging
        p1_diff, p2_diff = pegging_stage(
            player_1_hand_copy, player_2_hand_copy, p1_score, p2_score)
        p1_score += p1_diff
        p2_score += p2_diff
        print(f"{separator} Pegging done! Moving on! {separator}")
        print("\nSince player 2 has box, player 1 gets their hand scored first!")
        print("Hand:")
        p1_diff = hand_scoring(player_1_hand, cut_card)
        p1_score += p1_diff
        print(f"Points earned: {p1_diff}")
        print("\nNow player 2 gets their hand and then box scored!")
        print("Hand:")
        p2_diff = hand_scoring(player_2_hand, cut_card)
        p2_score += p2_diff
        print(f"Points earned: {p2_diff}")
        print("Box:")
        p2_diff = box_scoring(box, cut_card)
        p2_score += p2_diff
        print(f"Points earned: {p2_diff}")
        print(f"{separator} Scoring round completely finished! {separator}")

    print(f"Player 1: {p1_score}, Player 2: {p2_score}")
    return p1_score, p2_score


def main():
    """While no winner is decided: keeps looping rounds!"""
    base_deck = list(product(card_ranks, card_suits))
    player_1_score = 0
    player_2_score = 0
    round_number = 1
    # print("Base deck:")
    # print_deck(base_deck)
    p1_diff, p2_diff = round_functionality(base_deck, player_1_score,
                                           player_2_score, round_number)
    player_1_score += p1_diff
    player_2_score += p2_diff
    # print("Base deck after round:")
    # print_deck(base_deck)


if __name__ == "__main__":
    main()
