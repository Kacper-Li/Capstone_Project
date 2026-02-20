
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
