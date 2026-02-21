from card_utils import *
from pegging_functionality import *
import itertools

hand = [('5', 'Club'), ('3', 'Spade'), ('3', 'Heart'), ('3', 'Diamond'),
        ('5', 'Diamond')]
flush_hand = [('3', 'Club'), ('8', 'Club'), ('6', 'Club'), ('J', 'Club'),]
cut_card = ('5', 'Club')
card_pile = [('10', 'Club'), ('J', 'Club'), ('8', 'Heart')]


def find_all_fifteens(cards: list[Card]) -> list[str]:
    raw_cards = [card_value(card[0]) for card in cards]
    print(raw_cards)
    fifteens = []
    for value in range(len(raw_cards) + 1):
        combination = itertools.combinations(raw_cards, value)
        for combo in combination:
            # print(sum(combo))
            if sum(combo) == 15:
                fifteens.append('15 for two')
    return fifteens


def find_all_pairs(hand: list[Card]) -> list[str]:
    raw_cards = [card_value(card) for card in hand]
    pairs = []
    for value in card_ranks:
        counted = raw_cards.count(card_value((value, 'irrelevant')))
        if counted < 2:
            pass
        elif counted == 2:
            pairs.append('pair')
        elif counted == 3:
            pairs.append('pair royale')
        elif counted == 4:
            pairs.append('double pair royale')
    return pairs


def find_hand_flush(hand: list[Card], cut_card: Card) -> str:
    suit = [card[1] for card in hand]
    if suit.count(suit[1]) == 4:
        if cut_card[1] == suit[1]:
            return 'flush of 5'
        else:
            return 'flush of 4'
    else:
        return '0'


print()
# fifteens = find_all_fifteens(hand)
# pairs = find_all_pairs(hand)
# print(fifteens)
# print(pairs)
scores = 0
flush = find_hand_flush(flush_hand, cut_card)
# scores += sum([scoring_types[fifteen] for fifteen in fifteens])
# scores += sum([scoring_types[pair] for pair in pairs])
scores += scoring_types[flush]
print(flush)

print(scores)
print(hand)
