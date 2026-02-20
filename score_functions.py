from draft import Card
from draft import print_deck
from draft import scoring_types, card_suits, card_ranks


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
        score += run_check(cards[:])
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


def run_check(cards_played: list[Card]):
    """To check for a run, you MUST check every length combo.\n
    runs can break at any point, then be fixed by a new card\n
    e.g. 3 6 4 -> 3 6 4 5. or 1 2 3 6 -> 1 2 3 6 4 -> 1 2 3 6 4 5"""
    if len(cards_played) < 3:
        return 0
    print("Initial:")
    print_deck(cards_played)
    for i in range(3, len(cards_played) + 1):
        sorted_cards = sorted(cards_played[-i:], key=lambda card: card[0])
        print(f"In loop {i}:")
        print_deck(sorted_cards)


# IN CONCLUSION, YOU CALCULATE THE SCORE FROM CURRENT CARD.
# PREVIOUS SCORES ARE IRRELEVANT.

# Cribbage test hands covering edge cases
test0 = [('7', 'Heart'), ('7', 'Club')]
# Regular pair (2 points)
test1 = [('9', 'Heart'), ('9', 'Club'), ('9', 'Diamond')]
# Pair Royale / Three of a kind (6 points)
test2 = [('4', 'Heart'), ('4', 'Club'), ('4', 'Diamond'), ('4', 'Spade')]
# Double Pair Royale / Four of a kind (12 points)
test3 = [('3', 'Heart'), ('4', 'Club'), ('5', 'Diamond')]
# Regular run 3-4-5 (3 points)
test4 = [('3', 'Heart'), ('5', 'Club'), ('4', 'Diamond')]
# Run 3-4-5 out of order (3 points)
test5 = [('8', 'Heart'), ('7', 'Club')]
# Fifteen total: 8 + 7 = 15 (2 points)
test6 = [('3', 'Club'), ('2', 'Spade'), ('5', 'Diamond'),
         ('4', 'Heart'), ('7', 'Club'), ('6', 'Heart')]
# Run of six completely out of order: 3-2-5-4-7-6 (6 points)
test7 = [('10', 'Heart'), ('J', 'Club'),
         ('A', 'Diamond'), ('Q', 'Spade')]
# Total adding to 31 (2 points)
test8 = [('4', 'Heart'), ('7', 'Club'), ('6', 'Diamond'), ('5', 'Spade')]
# Run of four: 4-5-6-7 (4 points), total 22 < 31
test9 = [('7', 'Heart'), ('4', 'Club'), ('4', 'Diamond')]
# Pair + 15: pair of 4s (2 points), 11 + 4 = 15 (2 points)
test10 = [('6', 'Heart'), ('6', 'Club'), ('9', 'Diamond'), ('9', 'Spade')]
# Two pairs with a gap (2 points)

run_check(test6)
