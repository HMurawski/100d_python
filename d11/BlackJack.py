import os
import random


def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the total score of a hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares the scores of the player and the computer."""
    if user_score == computer_score:
        return "Draw :/"
    elif computer_score == 0:
        return "Lose, computer has Blackjack :("
    elif user_score == 0:
        return "You won with a Blackjack! "
    elif user_score > 21:
        return "You lose. Score over 21. "
    elif computer_score > 21:
        return "You won, opponent went over 21."
    elif user_score > computer_score:
        return "You win :)"
    else:
        return "You lose :/"


def play_game():
    """Plays a game of Blackjack."""
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial deal
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    input("Press Enter to continue...")
    clear_console()


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()
