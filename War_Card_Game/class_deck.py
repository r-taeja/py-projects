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
    
    def remove_top_card(self):
        """
        Function to remove the top card
        """
        return self.cards.pop(0)

    #Adding card
    def add_cards(self, *cards):         #what about duplicates?
        """
        Adds the card to the end of the list of cards/bottom of the deck.
        """
        self.cards.extend(cards)
    
    #Removing card
    def remove_cards(self, *cards_set):       
        # '*' accepts multiple arguments. But, giving a list as an argument is basically seen as one arument only. Doing for card in cards_set makes it see the entire list as one thing and doesn't access individual items of the list.
        #So, we want this function to accept input in the form of both lists, and multiple cards.
        #Removes only first occurence of the card if multiple same exist. To remove multiple, gotta provide list of them.
        """
        Removes the specific cards/list of cards from the deck.
        """
        for ele in cards_set:
            #If it is a list, unpack and remove cards given in list.
            if isinstance(ele, list):
                for card in ele:
                    self.cards.remove(card)
            
            #If given as individual cards, remove them directly.
            else:
                self.cards.remove(ele)

    #Counting the number of cards in the deck
    def count_deck(self):
        """
        Counts the number of cards present in the list of cards/deck.
        """
        return len(self.cards)
    
    #Drawing cards from the deck
    def draw_cards(self, count : int):             #How to deal alternate cards to players? What if more than two players?
        """
        Returns the first (count) number of cards from the front of the list/top of the deck as a list.
        """
        if not isinstance(count, int):
            raise KeyError("Count must be an integer.")

        if count > len(self.cards):
            raise ValueError("Not enough cards present in the deck to draw.")
        
        drawn_cards = self.cards[:count]
        self.remove_cards(drawn_cards)

        return drawn_cards
    
    def shuffle_cards(self):
        """
        Shuffles the items in the list of cards/cards in the deck.
        """
        random.shuffle(self.cards)


if __name__ == "__main__":

    c1 = Card(2, "Clubs")
    c2 = Card(3, "Clubs")
    c3 = Card(4, "Clubs")
    c4 = Card(5, "Clubs")
    c5 = Card(6, "Clubs")

    p_deck = Deck(c1, c2, c3, c4, c5)
    print(p_deck.show_cards())

    drawn_cards = p_deck.draw_cards(3)
    print(drawn_cards)