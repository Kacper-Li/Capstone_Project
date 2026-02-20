from card_utils import print_deck
from card_utils import Card
from card_utils import scoring_types
from card_utils import card_value
from run_score_calculator import find_biggest_run
from pair_score_calculator import find_biggest_pair


def pegging_scoring(cards: list[Card]) -> int:
    """Based on the very top card of the pile, calculates total score of card played."""
    score = 0
    total_card_rank = 0
    for card in cards:
        total_card_rank += card_value(card[0])
    if total_card_rank > 31:
        return -1
    elif total_card_rank == 15:
        score += 2
    elif total_card_rank == 31:
        score += 2
    print("Cards sending in: ")
    print_deck(cards)
    score += find_biggest_run(cards)
    # print(f"pair gives {scoring_types[find_biggest_pair(cards)]}")
    score += scoring_types[find_biggest_pair(cards)]
    print(f"Total score of card placed: {score}")
    return score


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

thirtyonewith15 = [('8', 'Heart'), ('7', 'Club'),
                   ('J', 'Heart'), ('6', 'Club')]
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
