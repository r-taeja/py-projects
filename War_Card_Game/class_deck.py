import random
from class_card import Card

class Deck:
    
    #initialising deck
    def __init__(self, *cards):
        """
        Initialises an instance of the deck with cards.
        """
        if len(cards) == 1 and isinstance(cards[0], list):
            self.cards = cards[0]
        else:
            self.cards = list(cards)

    def generate_full_deck(self):
        """
        Generates a full deck of 52 cards.
        """
        self.cards = [Card(value, suit) for value in Card.values for suit in Card.suits]

    #show cards
    def show_cards(self):
        """
        Returns the list of cards/shows the cards present in the deck.
        """
        return self.cards

    #result for printing out the instance
    def __repr__(self):
        """
        Returns the output of what should be printed when the deck object itself is printed.
        """
        return f"The deck contains {self.cards}"
    
    #Adding card
    def add_cards(self, *cards):         #what about duplicates?
        """
        Adds the card to the end of the list of cards/bottom of the deck.
        """
        self.cards.extend(cards)
    
    #Removing card
    def remove_card(self, *cards_set):      #*args for multiple cards? What about duplicates?
        """
        Removes the specific card from the list of cards/deck.
        """
        for card in cards_set:
            self.cards.remove(card)

    #Counting the number of cards in the deck
    def count_deck(self):
        """
        Counts the number of cards present in the list of cards/deck.
        """
        return len(self.cards)
    
    #Drawing cards from the deck
    def draw_cards(self, count):             #How to deal alternate cards to players? What if more than two players?
        """
        Returns the first (count) number of cards from the front of the list/top of the deck as a list.
        """
        if count > len(self.cards):
            raise ValueError("Not enough cards present in the deck to draw.")
        
        drawn_cards = self.cards[:count]
        for card in drawn_cards:
            self.remove_card(card)

        return drawn_cards
    
    def shuffle_cards(self):
        """
        Shuffles the items in the list of cards/cards in the deck.
        """
        random.shuffle(self.cards)


if __name__ == "__main__":

    c1 = (2, "Clubs")
    c2 = (3, "Clubs")
    c3 = (2, "Clubs")

    d = Deck(c1, c2, c3)
    print(d)