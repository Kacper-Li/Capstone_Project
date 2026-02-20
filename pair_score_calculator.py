from card_utils import Card
from card_utils import card_order
from card_utils import print_deck


def find_biggest_pair(cards_played: list[Card]) -> str:
    card_no = len(cards_played)
    if card_no < 2:
        return 0
    print("Started")
    print_deck(cards_played)
    cards_relevant = cards_played[:]
    if card_order(cards_relevant[-1][0]) != card_order(cards_relevant[-2][0]):
        return 0
    elif (card_no == 2):
        return 'pair'
    elif (card_no == 3):
        if card_order(cards_relevant[-2][0]) != card_order(cards_relevant[-3][0]):
            return 'pair'
        else:
            return 'pair royale'
    elif (card_no == 4):
        if card_order(cards_relevant[-3][0]) != card_order(cards_relevant[-4][0]):
            return 'pair royale'
        else:
            return 'double pair royale'
    else:
        return 'Not supposed to happen'


pair0 = [('7', 'Heart'), ('7', 'Club')]
# Regular pair (2 points)
pair1 = [('9', 'Heart'), ('9', 'Club'), ('9', 'Diamond')]
# Pair Royale / Three of a kind (6 points)
pair2 = [('4', 'Heart'), ('4', 'Club'), ('4', 'Diamond'), ('4', 'Spade')]
# Double Pair Royale / Four of a kind (12 points)
pair3 = [('6', 'Heart'), ('6', 'Club'), ('9', 'Diamond'), ('9', 'Spade')]
# Two pairs with a gap (2 points)

test = find_biggest_pair(pair0)
print(f"Found: {test}")
test = find_biggest_pair(pair1)
print(f"Found: {test}")
test = find_biggest_pair(pair2)
print(f"Found: {test}")
test = find_biggest_pair(pair3)
print(f"Found: {test}")
