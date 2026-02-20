from draft import Card
from draft import print_deck
from run_score_calculator import find_biggest_run


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


def scoring(cards: list[Card]) -> int:
    amount = len(cards)
    score = 0
    if amount == 1:
        return 0
    elif amount == 2:
        if cards[0][0] == cards[1][0]:
            score += scoring_types['pair']
        if cards[0][0] + cards[1][0] == 15:
            score += scoring_types['15 for two']
    elif amount == 3:
        if cards[1][0] == cards[2][0]:
            if cards[0][0] == cards[1][0]:
                score += scoring_types['pair royale']
            else:
                score += scoring_types['pair']
        score += find_biggest_run(cards[:])
    elif amount == 4:
        "check all but flush and 5run"
    elif amount == 5:
        "check all but 6 run"
    elif amount == 6:
        "check all but 7 run"
    elif amount == 7:
        "check everything"
    elif amount == 8:
        "check everything"
    else:
        return 0
