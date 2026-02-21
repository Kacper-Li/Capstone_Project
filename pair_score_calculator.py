from card_utils import Card
from card_utils import card_order
from card_utils import card_value
from card_utils import card_ranks
from card_utils import print_deck


def find_biggest_pair(cards_played: list[Card]) -> str:
    card_no = len(cards_played)
    if card_no < 2:
        return '0'
    # print("Pair function begins")
    # print_deck(cards_played)
    cards_relevant = cards_played[:]

    if card_order(cards_relevant[-1]) != card_order(cards_relevant[-2]):
        return '0'
    elif (card_no > 2):
        if card_order(cards_relevant[-2]) != card_order(cards_relevant[-3]):
            return 'pair'
        elif (card_no > 3):
            if card_order(cards_relevant[-3]) != card_order(cards_relevant[-4]):
                return 'pair royale'
            else:
                return 'double pair royale'
        else:
            return 'pair royale'
    else:
        return 'pair'


def find_all_pairs(hand: list[Card]) -> list[str]:
    """Returns all pairs found as a list of score rules."""
    raw_cards = [card_order(card) for card in hand]
    pairs = []
    for value in card_ranks:
        # print("Value:", value)
        counted = raw_cards.count(card_order((value, 'irrelevant')))
        # print("Counted:", counted)
        if counted < 2:
            pass
        elif counted == 2:
            pairs.append('pair')
        elif counted == 3:
            pairs.append('pair royale')
        elif counted == 4:
            pairs.append('double pair royale')
    return pairs


pair0 = [('7', 'Heart'), ('7', 'Club')]
# Regular pair (2 points)
pair1 = [('9', 'Heart'), ('9', 'Club'), ('9', 'Diamond')]
# Pair Royale / Three of a kind (6 points)
pair2 = [('4', 'Heart'), ('4', 'Club'), ('4', 'Diamond'), ('4', 'Spade')]
# Double Pair Royale / Four of a kind (12 points)
pair3 = [('6', 'Heart'), ('6', 'Club'), ('9', 'Diamond'), ('9', 'Spade')]
# Two pairs with a gap (2 points)
test0 = [('3', 'Spade'), ('10', 'Heart'), ('A', 'Heart')]
# A logical glitch sees 10 and A as the same

# Tests:
# test = find_biggest_pair(pair0)
# print(f"Found: {test}")
# test = find_biggest_pair(pair1)
# print(f"Found: {test}")
# test = find_biggest_pair(pair2)
# print(f"Found: {test}")
# test = find_biggest_pair(test0)
# print(f"Found: {test}")

# hand1 = [('6', 'Diamond'), ('2', 'Heart'), ('J', 'Heart'), ('K', 'Heart')]
# hand2 = [('7', 'Club'), ('7', 'Heart'), ('4', 'Diamond'), ('4', 'Heart')]
# hand1.append(('K', 'Club'))
# x = find_all_pairs(hand1)
# print(x)
