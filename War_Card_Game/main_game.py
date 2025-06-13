from class_card import Card
from class_deck import Deck
from game_logic import *

#Dealing cards to user and computer

#Generating and shuffling dealer's deck 
dealer_deck = Deck()
dealer_deck.generate_full_deck()
dealer_deck.shuffle_cards()

#Draw half of the deck for the user
user_cards = dealer_deck.draw_cards(26)
user_deck = Deck(user_cards)

#Draw next half of the deck for the computer
comp_cards = dealer_deck.draw_cards(26)
comp_deck = Deck(comp_cards)


#Opening message
print("\n ===================================================")
print("|                       WAR                         |")
print(" ===================================================")

print("\n============== \033[4mLET'S START THE BATTLE\033[0m ==============\n")

#Start the game
play_round(user_deck, comp_deck)

#Results of the game
print("\n=================== \033[4mFINAL RESULTS\033[0m ===================\n")

print(f"You have a total of {user_deck.count_deck()} cards.")
print(f"The computer has a total of {comp_deck.count_deck()} cards.")
print("\n")

#Player with higher number of cards is the winner
if user_deck.count_deck() > comp_deck.count_deck():
    print("You have more cards remaining than the computer.")
    print("YOU WIN!!!")
    
elif user_deck.count_deck() < comp_deck.count_deck():
    print("The computer has more cards remaining than you.")
    print("COMPUTER WINS!!!")

else:
    print("Both players have equal number of cards remaining.")
    print("IT's A TIE!!!")

print("\n")