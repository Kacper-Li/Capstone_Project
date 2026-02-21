from card_utils import Card
from card_utils import print_deck
from card_utils import card_order


# To check for a run, you MUST check every length combo.\n
# runs can break at any point, then be fixed by a new card\n
# e.g. 3 6 4 -> 3 6 4 5. or 1 2 3 6 -> 1 2 3 6 4 -> 1 2 3 6 4 5\n
# In order to find the correct run in a sequence,\n
# you must look for the highest possible run achieved.\n
# e.g. a run of 4 is void if apart of a run of 6.\n
# e.g. last 4 cards: 3 1 4 2 last 6 cards: 6 5 3 1 4 2
def is_run(sorted_cards: list[Card]) -> int:
    """Function to specifically check if input cards make a run.\n
    Returns the length of found run, otherwise 0 for no run found."""
    for j in range(len(sorted_cards) - 1, 0, -1):
        # print(sorted_cards[j])
        if card_order(sorted_cards[j]) - card_order(sorted_cards[j-1]) != 1:
            # print(f"Should break here with {sorted_cards[j-1]}")
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
            cards_played[i:], key=lambda card: card_order(card))
        # print(f"In loop {len(cards_played) - i}:")
        # print_deck(sorted_cards)
        run_count = is_run(sorted_cards)
        # print(f"The run count returned is {run_count} here")
        if run_count > 2:
            return run_count
        # print(f"Card about to be removed from search is {cards_played[i]}")
    # print("Reached end of run calculator")
    return 0


# IN CONCLUSION, YOU CALCULATE THE SCORE FROM CURRENT CARD.
# PREVIOUS SCORES ARE IRRELEVANT.
# Cribbage test hands covering edge cases

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
thirtyonewith15 = [('8', 'Heart'), ('7', 'Club'),
                   ('J', 'Heart'), ('6', 'Club')]
# 15 + 31: 8 + 7 = 15, total is 31 (4 points)


# Tests:
# run_pts = find_biggest_run(thirtyonewith15)
# print(f"The amount of points this run has is {run_pts}")
# run_pts = find_biggest_run(run1)
# print(f"The amount of points this run has is {run_pts}")
# run_pts = find_biggest_run(run2)
# print(f"The amount of points this run has is {run_pts}")
# run_pts = find_biggest_run(run3)
# print(f"The amount of points this run has is {run_pts}")
# test3 = [('A', 'Spade'), ('9', 'Spade'), ('9', 'Heart'), ('8', 'Diamond')]
# out = find_biggest_run(test3)
# print(f"The amount of points this run has is {out}")
# test4 = [('3', 'Diamond'), ('K', 'Diamond'),
#          ('2', 'Diamond'), ('10', 'Heart'), ('3', 'Spade')]
# out = find_biggest_run(test4)
# print(f"The amount of points this run has is {out}")
