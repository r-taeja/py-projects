
def resolve_war(user_deck, comp_deck, war_pile = None):
    """
    Resolves the War
    """
    if war_pile is None:
        war_pile = []

    #Check if either of the players have enough cards to go to war
    #Since I only print out top card of the list and don't remove it, 
    #I need to check if the deck has a total of 5 cards remaining.
    #That is, 1(the card that caused the draw) + 3 (face down) + 1 (to check for tie-breaker).
    if user_deck.count_deck() < 5 or comp_deck.count_deck() < 5:
        #Player with higher number of cards is the winner
        if user_deck.count_deck() > comp_deck.count_deck():
            print("USER WINS!!!")
        else:
            print("COMPUTER WINS!!!")

        return

    #If players can play the war, let them know
    print("This is a tie.")
    print("Three cards have been drawn from each of your decks.\n")

    #Both parties have to let go of these cards, and winner gets the pile
    war_pile.extend(user_deck.draw_cards(4) + comp_deck.draw_cards(4))

    print("Next cards : \n")
    #Get the fourth card (three cards face down, next card face up)
    user_card = user_deck.cards[0]
    comp_card = comp_deck.cards[0]

    print(f"Your card : {user_card}")
    print(f"Computer's card : {comp_card}\n")

    #Compare each of the new cards
    if user_card.get_value_num() > comp_card.get_value_num():

        comp_deck.remove_card(comp_card)                    #Comp removes the card played from its deck
        user_deck.remove_card(user_card)                    #User removes the card played from their deck
        war_pile.extend([comp_card, user_card])             #Adding both the top cards to the war pile.  Convert to list so extend takes in as only 1 argument instead of 2 in case of .extend(comp_card, user_card)
        user_deck.add_cards(*war_pile)                      #user wins all war_pile cards. Use * to unpack list of elements into individual ones.
            
        print(f"User wins this round.\n")

        #printing number of cards after the exchange
        print(f"You have {user_deck.count_deck()} cards remaining.")
        print(f"The computer has {comp_deck.count_deck()} cards remaining.")
        print("\n")
        
        #asking user if they'd like to continue playing the game
        MoveOn = str(input("Do you want to continue? (y/n) "))
        if MoveOn == "y":
            print("\n")
        else:
            return

    elif user_card.get_value_num() < comp_card.get_value_num():

        user_deck.remove_card(user_card)                    #User removes the card from their deck
        comp_deck.remove_card(comp_card)                    #Comp removes its card its deck
        war_pile.extend([user_card, comp_card])             #Adding both cards to the war_pile. Convert to list so extend takes in as only 1 argument instead of 2 in case of .extend(user_card, comp_card)
        comp_deck.add_cards(*war_pile)                      #Comp gets all war_pile cards. Use * to unpack list of elements into individual ones.

        print(f"Computer wins this round.\n")

        #printing number of cards after the exchange
        print(f"You have {user_deck.count_deck()} cards remaining.")
        print(f"The computer has {comp_deck.count_deck()} cards remaining.")
        print("\n")

        #asking user if they'd like to continue playing the game
        MoveOn = str(input("Do you want to continue? (y/n) "))
        if MoveOn == "y":
            print("\n")
            pass
        else:
            return

    else:
        resolve_war(user_deck, comp_deck, war_pile)

def play_round(user_deck, comp_deck, round_no = 1):
    """
    Plays each round according to game logic.
    """
    
    #Base Case
    if user_deck.count_deck() == 0 or comp_deck.count_deck() == 0:
        if user_deck.count_deck() > comp_deck.count_deck():
            print("The computer has no cards left to play. The game is thus over.")
        
        elif comp_deck.count_deck() > user_deck.count_deck():
            print("You have no cards left to play. The game is thus over.")
        
        else:
            print("Both parties have no cards left to play. The game is thus over.")

    while (user_deck.count_deck() > 0 and comp_deck.count_deck() > 0) :
        
        #Keeping track of the round number
        print(f"\n============== \033[4mROUND {round_no}\033[0m ==============\n")

        #Checking the top card
        user_card = user_deck.cards[0]
        comp_card = comp_deck.cards[0]
        
        print(f"Your card : {user_card}")
        print(f"Computer's card : {comp_card}\n")

        #If user card is greater than comp card -> user gets comp card added to his deck at the bottom and pushes his card to the bottom.
        if (user_card.get_value_num() > comp_card.get_value_num()):

            won_card = comp_card
            comp_deck.remove_card(won_card)     #Comp gets card removed from its deck
            user_deck.remove_card(user_card)    #User removes his card from the top of the deck
            user_deck.add_cards(won_card)       #User gets comp's card added to their deck at the bottom
            user_deck.add_cards(user_card)      #User places his card at the bottom

            print(f"User wins this round.\n")

            #printing number of cards after the exchange
            print(f"You have {user_deck.count_deck()} cards remaining.")
            print(f"The computer has {comp_deck.count_deck()} cards remaining.")
            print("\n")
            
            #asking user if they'd like to continue playing the game
            MoveOn = str(input("Do you want to continue? (y/n) "))
            if MoveOn == "y":
                print("\n")
            else:
                break


    #     elif user_card < comp_card:
    #         user_car, comp_card -> bottom of comp deck (data structure? order?)
    #         count_comp_deck + 1, count_user_deck - 1

        #If comp card is greater than user card, comp gets user card added to its deck at the bottom and moves its card to the bottom
        elif (user_card.get_value_num() < comp_card.get_value_num()):
            won_card = user_card
            user_deck.remove_card(won_card)     #User gets card removed from their deck
            comp_deck.remove_card(comp_card)    #Comp gets card removed from its deck
            comp_deck.add_cards(won_card)       #Comp gets user's card added to its deck bottom at the bottom
            comp_deck.add_cards(comp_card)      #Comp placed its card at the bottom

            print(f"Computer wins this round.\n")

            #printing number of cards after the exchange
            print(f"You have {user_deck.count_deck()} cards remaining.")
            print(f"The computer has {comp_deck.count_deck()} cards remaining.")
            print("\n")
            
            #asking user if they'd like to continue playing the game
            MoveOn = str(input("Do you want to continue? (y/n) "))
            if MoveOn == "y":
                print("\n")
                pass
            else:
                break

    #     else:
    #         draw_user_deck*3, draw_comp_deck*3
    #         draw_user_deck, draw_comp_deck
    #         repeat above test with the latest cards, but add all cards to the winner.
        else:
            resolve_war(user_deck, comp_deck)
        
        #Next Round
        round_no += 1