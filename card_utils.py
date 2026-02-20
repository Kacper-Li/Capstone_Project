import random

scoring_types = {
    'type': "score_value",
    '15 for two': 2,
    'pair': 2,
    'pair royale': 6,
    'double pair royale': 12,
    'run of 3': 3,
    'run of 4': 4,
    'run of 5': 5,
    'run of 6': 6,
    'run of 7': 7,
    'flush of 4': 4,  # impossible in box and pegging
    'flush of 5': 5,  # only if flush of 4 first in hand
    'One for go': 1,
    '31 for two': 2,
    '2 for his heels': 2,
    '1 for his nobs': 1,
}


Card = tuple[str, str]

card_suits = ['Club', 'Diamond', 'Heart', 'Spade']
card_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def card_value(card: Card) -> int:
    """Returns proper card values, as according to pegging values."""
    if card in ['Q', 'J', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def card_order(card: Card) -> int:
    """Returns correct order of cards, for run calculation"""
    if card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 1
    else:
        return int(card)


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


def pick_a_card(card_set: list[Card], index=0) -> Card:
    """
    Remove and return a random (rank, suit) card from any card_set.\n
    Manipulates the list of cards directly.
    """
    pick_a_card = card_set.pop(random.randint(0, len(card_set) - 1))
    # print(f"The card chosen at random: {pick_a_card[0]} of {pick_a_card[1]}s")
    return pick_a_card
