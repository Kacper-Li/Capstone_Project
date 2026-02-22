from card_utils import *
from pegging_functionality import *
from scoring_calculation import hand_scoring

hand = [('3', 'Spade'), ('3', 'Heart'), ('3', 'Diamond'), ('5', 'Diamond')]
flush_hand = [('3', 'Club'), ('8', 'Club'), ('6', 'Club'), ('J', 'Club'),]
cut_card = ('5', 'Club')
card_pile = [('10', 'Club'), ('J', 'Club'), ('8', 'Heart')]


print()
scores = 0
hand_score = hand_scoring(hand, cut_card)
print(hand_score)
print(scores)
print(hand)
