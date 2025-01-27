import random

# Deck of cards
deck_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Deal a random card
def deal():
    return random.choice(deck_of_cards)

# Main Blackjack game logic
def play_blackjack():
    player_hand = []
    computer_hand = []

    # Deal initial cards
    for _ in range(2):
        player_hand.append(deal())
        computer_hand.append(deal())

    # Calculate totals
    player_total = sum(player_hand)
    computer_total = sum(computer_hand)

    # Display initial cards
    print(f"Your cards: {player_hand}, current total: {player_total}")
    print(f"Computer's first card: {computer_hand[0]}")

    # Allow player to draw additional cards
    while player_total < 21:
        draw = input("Type 'y' to draw another card, or 'n' to pass: ").lower()
        if draw == 'y':
            new_card = deal()
            player_hand.append(new_card)
            player_total = sum(player_hand)
            print(f"You drew a {new_card}. Your cards: {player_hand}, current total: {player_total}")
        else:
            break

    # Computer's turn (simple logic: draw if total < 17)
    while computer_total < 17:
        new_card = deal()
        computer_hand.append(new_card)
        computer_total = sum(computer_hand)

    # Reveal results
    print(f"Your final hand: {player_hand}, final total: {player_total}")
    print(f"Computer's final hand: {computer_hand}, final total: {computer_total}")

    # Determine winner
    if player_total > 21:
        print("You went over 21. You lose!")
    elif computer_total > 21 or player_total > computer_total:
        print("You win!")
    elif player_total < computer_total:
        print("Computer wins!")
    else:
        print("It's a draw!")

# Start game
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play_game == 'y':
    play_blackjack()
else:
    print("Maybe next time!")
