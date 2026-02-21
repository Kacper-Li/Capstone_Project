from card_utils import *
from pegging_functionality import *


hand = [('2', 'Club'), ('9', 'Spade'), ('1', 'Heart'), ('Q', 'Diamond'),
        ('3', 'Diamond'), ('J', 'Diamond')]
card_pile = [('10', 'Club'), ('J', 'Club'), ('8', 'Heart')]


playable_cards = can_place(hand, card_pile)
print("Playable: ", playable_cards)
card_to_play = random.choice(playable_cards)
# how to specify to pick from hand something in
print(card_to_play)
hand.remove(card_to_play)
card_pile.append(card_to_play)

print()
print(card_pile)
print(hand)
