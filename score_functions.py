from draft import Card
from draft import print_deck
from draft import scoring_types, card_suits, card_ranks


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


# To check for a run, you MUST check every length combo.\n
# runs can break at any point, then be fixed by a new card\n
# e.g. 3 6 4 -> 3 6 4 5. or 1 2 3 6 -> 1 2 3 6 4 -> 1 2 3 6 4 5\n
# In order to find the correct run in a sequence,\n
# you must look for the highest possible run achieved.\n
# e.g. a run of 4 is void if apart of a run of 6.\n
# e.g. last 4 cards: 3 1 4 2 last 6 cards: 6 5 3 1 4 2
def is_run(sorted_cards: list[Card]) -> int:
    """Function to specifically check if input cards make a run."""
    for j in range(len(sorted_cards) - 1, 0, -1):
        print(sorted_cards[j])
        if card_order(sorted_cards[j][0]) - card_order(sorted_cards[j-1][0]) != 1:
            print(f"Should break here with {sorted_cards[j-1]}")
            return 0
    return len(sorted_cards)


def find_biggest_run(cards_played: list[Card]) -> int:
    """Checks for the largest run in supplied cards_played pile."""
    if len(cards_played) < 3:
        return 0
    # print("Initial:")
    # print_deck(cards_played)
    # print("")
    for i in range(0, len(cards_played) - 1):
        sorted_cards = sorted(
            cards_played[i:], key=lambda card: card_order(card[0]))
        # print(f"In loop {len(cards_played) - i}:")
        print_deck(sorted_cards)
        run_count = is_run(sorted_cards)
        print(f"The run count is {run_count} here")
        if run_count > 0:
            return run_count
        print(f"Card about to be removed from search is {cards_played[i]}")


# IN CONCLUSION, YOU CALCULATE THE SCORE FROM CURRENT CARD.
# PREVIOUS SCORES ARE IRRELEVANT.
# Cribbage test hands covering edge cases
pair0 = [('7', 'Heart'), ('7', 'Club')]
# Regular pair (2 points)
pair1 = [('9', 'Heart'), ('9', 'Club'), ('9', 'Diamond')]
# Pair Royale / Three of a kind (6 points)
pair2 = [('4', 'Heart'), ('4', 'Club'), ('4', 'Diamond'), ('4', 'Spade')]
# Double Pair Royale / Four of a kind (12 points)
pair3 = [('6', 'Heart'), ('6', 'Club'), ('9', 'Diamond'), ('9', 'Spade')]
# Two pairs with a gap (2 points)

run0 = [('3', 'Heart'), ('4', 'Club'), ('5', 'Diamond')]
# Regular run 3-4-5 (3 points)
run1 = [('3', 'Heart'), ('5', 'Club'), ('4', 'Diamond')]
# Run 3-4-5 out of order (3 points)
run2 = [('3', 'Club'), ('2', 'Spade'), ('5', 'Diamond'),
        ('4', 'Heart'), ('7', 'Club'), ('6', 'Heart')]
# Run of six completely out of order: 3-2-5-4-7-6 (6 points)
run3 = [('4', 'Heart'), ('7', 'Club'), ('6', 'Diamond'), ('5', 'Spade')]
# Run of four: 4-5-6-7 (4 points), total 22 < 31

fifteen5 = [('8', 'Heart'), ('7', 'Club')]
# Fifteen total: 8 + 7 = 15 (2 points)
thirtyone0 = [('10', 'Heart'), ('J', 'Club'),
              ('A', 'Diamond'), ('Q', 'Spade')]
# Total adding to 31 (2 points)

pairwith15 = [('7', 'Heart'), ('4', 'Club'), ('4', 'Diamond')]
# Pair + 15: pair of 4s (2 points), 11 + 4 = 15 (2 points)


run_pts = find_biggest_run(run0)
print(f"The amount of points this run has is {run_pts}")
run_pts = find_biggest_run(run1)
print(f"The amount of points this run has is {run_pts}")
run_pts = find_biggest_run(run2)
print(f"The amount of points this run has is {run_pts}")
run_pts = find_biggest_run(run3)
print(f"The amount of points this run has is {run_pts}")
