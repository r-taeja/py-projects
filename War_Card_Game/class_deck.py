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
        drawn_cards = self.cards[:count]
        for card in drawn_cards:
            self.remove_card(card)

        return drawn_cards
    
    def shuffle_cards(self):
        """
        Shuffles the items in the list of cards/cards in the deck.
        """
        random.shuffle(self.cards)

    def resolve_war(self, user_deck, comp_deck, depth = 1):
        """
        Resolves the War
        """
        #Check if either of the players have enough cards to go to war
        if user_deck.count_deck() < 4 or comp_deck.count_deck() < 4:

            #Player with higher number of cards is the winner
            if user_deck.count_deck() > comp_deck.count_deck():
                print("USER WINS!!!")
            
            else:
                print("COMPUTER WINS!!!")

        #Get the fourth card (three cards face down, next card face up)
        user_card = user_deck.show_cards()[0+((3+1)*depth)]
        comp_card = comp_deck.show_cards()[0+((3+1)*depth)]

        #Compare each of the new cards
        if user_card.get_value_num() > comp_card.get_value_num():

            #Comp moves
            comp_deck.remove_card(comp_card)                    #Comp removes the top card played from its deck
            won_cards = comp_deck.draw_cards((1+3)*depth)       #Comp removes the remaining 4 cards - one from previous round and three face down

            #User moves
            user_deck.remove_card(user_card)                    #User removes the top card played from their deck
            user_cards = user_deck.draw_cards((1+3)*depth)      #User removes the remaining 4 cards - one from previous round and three face down
            user_deck.add_cards(comp_card)                      #User adds comp's top card
            for card in won_cards:                              #user adds comp's four cards
                user_deck.add_cards(card)          
            user_deck.add_cards(user_card)                      #User adds user's card that got them to win the tie
            for card in user_cards:                             #user adds user's four cards
                user_deck.add_cards(card)

        elif user_card.get_value_num() < comp_card.get_value_num():

            #Comp moves
            user_deck.remove_card(user_card)                    #User removes the card from its deck
            won_cards = user_deck.draw_cards((1+3)*depth)       #User removes the other 4 cards - one from previous round and three face down

            #User moves
            comp_deck.remove_card(comp_card)                    #Comp removes the top card played from its deck
            comp_cards = comp_deck.draw_cards((1+3)*depth)      #Comp removes the remaining 4 cards - one from previous round and three face down
            comp_deck.add_cards(user_card)                      #Comp adds user's top card
            for card in won_cards:                              #Comp adds user's four cards
                comp_deck.add_cards(card)          
            comp_deck.add_cards(comp_card)                      #Comp adds comp's card that got it to win the tie
            for card in comp_cards:                             #Comp adds comp's four cards
                comp_deck.add_cards(card)

        else:
            #Call the same function again, with depth increased to 2.
            #The depth helps because the cards go up in the pattern ((1+3)*depth). :)
            depth+=1
            Deck.resolve_war(user_deck, comp_deck, depth)


if __name__ == "__main__":

    # if user_card.get_value_num() == comp_card.get_value_num():
    #     #Go 3 cards ahead
    #     user_card = user_deck.show_cards()[0+3+1]
    #     comp_card = comp_deck.show_cards()[0+3+1]
    #     if user_card.get_value_num() > comp_card.get_value_num():

    #         #Comp moves
    #         comp_deck.remove_card(comp_card)        #Comp removes the card from its deck
    #         won_cards = comp_deck.draw_cards(1+3)   #Comp removes the other 4 cards

    #         #User moves
    #         user_deck.remove_card(user_card)        #User removes the card from the deck
    #         user_cards = user_deck.draw_cards(1+3)  #User removes the other 4 cards
    #         user_deck.add_cards(comp_card)          #User adds comp's top card
    #         for card in won_cards:                  #user adds comp's four cards
    #             user_deck.add_cards(card)          
    #         user_deck.add_cards(user_card)          #User adds user's card that got him to win the tie
    #         for card in won_cards:                  #user adds user's four cards
    #             user_deck.add_cards(card)

    #     if user_card.get_value_num() < comp_card.get_value_num():

    #         #Comp moves
    #         user_deck.remove_card(user_card)        #User removes the card from its deck
    #         won_cards = user_deck.draw_cards(1+3)   #User removes the other 4 cards

    #         #User moves
    #         comp_deck.remove_card(comp_card)        #Comp removes the card from the deck
    #         comp_cards = comp_deck.draw_cards(1+3)  #Comp removes the other 4 cards
    #         comp_deck.add_cards(user_card)          #Comp adds user's top card
    #         for card in won_cards:                  #Comp adds user's four cards
    #             comp_deck.add_cards(card)          
    #         comp_deck.add_cards(comp_card)          #Comp adds comp's card that got him to win the tie
    #         for card in won_cards:                  #Comp adds comp's four cards
    #             comp_deck.add_cards(card)

    #     if user_card.get_value_num() == comp_card.get_value_num():
    #         #Draw three cards again, and COMPARE next card
    #         user_card = user_deck.show_cards()[0+3+1+3+1]
    #         comp_card = comp_deck.show_cards()[0+3+1+3+1]
            
    #         #Compare them again. This is recursive. Gotta make a function of sorts and figure out how to loop with index "i"...

    c1 = Card(2, "Spades")
    c2 = Card("Ace", "Diamonds")
    c3 = Card(7, "Clubs")
    c4 = Card(3, "Diamonds")
    c5 = Card(9, "Hearts")
    c6 = Card(2, "Hearts")
    c7 = Card("King", "Hearts")
    c8 = Card("Jack", "Hearts")
    c9 = Card(8, "Clubs")
    c10 = Card(5, "Diamonds")

    user_deck = Deck(c1, c2, c3, c4, c5)
    comp_deck = Deck(c6, c7, c8, c9, c10)

    print(f"User's deck : {user_deck}")
    print(f"Comp's deck : {comp_deck}")

    while (user_deck.count_deck() > 0 and comp_deck.count_deck() > 0) :
        #Checking the top card
        user_card = user_deck.cards[0]
        comp_card = comp_deck.cards[0]
        
        #If user card is greater than comp card -> user gets comp card added to his deck at the bottom and pushes his card to the bottom.
        if (user_card.get_value_num() > comp_card.get_value_num()):
            won_card = comp_card
            comp_deck.remove_card(won_card)     #Comp gets card removed from its deck
            user_deck.remove_card(user_card)    #User removes his card from the top of the deck
            user_deck.add_cards(won_card)       #User gets comp's card added to their deck at the bottom
            user_deck.add_cards(user_card)      #User places his card at the bottom

            #printing decks after the exchange
            print(f"User's deck : {user_deck}")
            print(f"Computer's deck : {comp_deck}")
                  
            print(f"The user has {user_deck.count_deck()} cards remaining.")
            print(f"The computer has {comp_deck.count_deck()} cards remaining.")
            
            #asking user if they'd like to continue playing the game
            MoveOn = str(input("Do you want to continue? (y/n) "))
            if MoveOn == "y":
                print("\n")
                pass
            else:
                break

        #If comp card is greater than user card, comp gets user card added to its deck at the bottom and moves its card to the bottom
        elif (user_card.get_value_num() < comp_card.get_value_num()):
            won_card = user_card
            user_deck.remove_card(won_card)     #User gets card removed from their deck
            comp_deck.remove_card(comp_card)    #Comp gets card removed from its deck
            comp_deck.add_cards(won_card)       #Comp gets user's card added to its deck bottom at the bottom
            comp_deck.add_cards(comp_card)      #Comp placed its card at the bottom

            #printing decks after the exchange
            print(f"User's deck : {user_deck}")
            print(f"Computer's deck : {comp_deck}")
                  
            print(f"The user has {user_deck.count_deck()} cards remaining.")
            print(f"The computer has {comp_deck.count_deck()} cards remaining.")

            #asking user if they'd like to continue playing the game
            MoveOn = str(input("Do you want to continue? (y/n) "))
            if MoveOn == "y":
                print("\n")
                pass
            else:
                break
        
        #If tie, resolve the war.
        else:
            user_deck.resolve_war(user_deck, comp_deck)

    # print("\n=================== \033[4mFINAL RESULTS\033[0m ===================\n")
    # print(f"User's deck : {user_deck.show_cards()}")
    # print(f"Computer's deck : {comp_deck.show_cards()}")
    # print("\n")