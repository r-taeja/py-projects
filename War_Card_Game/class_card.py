class Card:
    #Class-level constants
    values  = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
    value_num = {value_num : index for index, value_num in enumerate(values, start = 1)}

    def __init__(self, value, suit):
        """
        Initialising the card with a valid value and suit.
        """
        #Checking if value is valid.
        if value not in self.values or not value:
            raise ValueError("The card must have a non-empty valid value (\"Ace\", \"King\", \"Queen\", \"Jack\", 2, 3, 4, 5, 6, 7, 8, 9, 10).")
        
        #Checking if suit is valid.
        if suit not in self.suits or not suit:
            raise ValueError("The card must have a non-empty valid suit (\"Diamonds\", \"Spades\", \"Clubs\", \"Hearts\").")
        
        self.value = value
        self.suit = suit

    def get_value(self):
        """
        Returns the value of the card.
        """
        return self.value
    
    def get_suit(self):
        """
        Returns the suit of the card.
        """
        return self.suit
    
    def __repr__(self):     
        """
        This will tell how to print out cards (instead of object <...>).
        """
        return f"{self.get_value()} of {self.get_suit()}"
    
    def get_value_num(self):
        """
        Returns the numerical value/score of the card as per the rules of the 
        game (2 - 10 : 1 - 9; Jack - Ace : 10 - 13).
        """
        return self.value_num[self.get_value()]
        

if __name__ == "__main__": 
    c1 = Card(2, "Spades")
    c2 = Card("Ace", "Diamonds")

    print(c1.get_value_num() > c2.get_value_num())