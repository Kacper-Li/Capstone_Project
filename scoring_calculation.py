from card_utils import Card
from card_utils import print_deck
from card_utils import scoring_types
from run_score_calculator import find_biggest_run
from pair_score_calculator import find_biggest_pair


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
