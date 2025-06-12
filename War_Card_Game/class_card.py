class Card:

    def __init__(self, value, suit):
        """
        Initialising the card with a valid value and suit.
        """
        
        values  = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        suits = ["Diamonds", "Spades", "Clubs", "Hearts"]

        #Checking if value is valid.
        if value not in values or not value:
            raise ValueError("The card must have a non-empty valid value (\"Ace\", \"King\", \"Queen\", \"Jack\", 2, 3, 4, 5, 6, 7, 8, 9, 10).")
        
        #Checking if suit is valid.
        if suit not in suits or not suit:
            raise ValueError("The card must have a non-empty valid suit (\"Diamonds\", \"Spades\", \"Clubs\", \"Hearts\").")
        
        self.value = value
        self.suit = suit
        self.value_num = {index : value_num for value_num, index in enumerate(values, start = 1)}

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
        return self.value_num[self.get_value()]
        

if __name__ == "__main__": 
    c1 = Card(2, "Spades")
    c2 = Card("Ace", "Diamonds")

    print(c1.get_value_num() > c2.get_value_num())