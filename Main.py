#Blackjack
import random


deck_of_cards = ['A', '2', '3', '4', '5', '6', '7', '8','9', '10', 'J', 'Q', 'K']
player1 = []
computer = []
i = 0

def deal():
    select_card = random.choices(deck_of_cards)
    return select_card

play_Blackjack = input("Do you want to play a game of BlackJack? Type 'y' or 'n' ").lower()
if play_Blackjack == "y":    
    while i < 2:
        first_player = deal()
        first_computer = deal()
        player1.append(first_player)
        computer.append(first_computer)
        i += 1
    print(player1)
    print(computer)
    add_card = True
    
    
    while add_card == True:
        user_select = input("Would you like to add a card? 'Y' or 'N' ").lower()    
        if user_select == "y":
            card1 = deal()
            player1.append(card1)
            print(player1)
        elif user_select == "n":
            print(player1)  
            print(computer)
            add_card == False
else:
    print("Thank You! ")
        
        
        #add winning and losing condintions