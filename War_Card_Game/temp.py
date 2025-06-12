from class_card import Card
from class_deck import Deck


values = ["Ace", "King", "Queen", "Jack", 2, 3, 4, 5, 6, 7, 8, 9, 10]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
all_cards = [Card(i, j) for i in values for j in suits]

all_deck = Deck(all_cards)

print(all_deck)