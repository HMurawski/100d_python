import random

def count_attempts(remaining_lives, continue_game):
    player_guess = int(input("Make a guess: "))
    if player_guess == picked_number:
        print(f"You won! You made a correct guess! ")
        continue_game = False
    elif player_guess != picked_number:
        remaining_lives -= 1
        if player_guess > picked_number:
            print("Too high.")
        else:
            print("Too low.")
        print(f"You have {remaining_lives} attempts remaining. ")
        if remaining_lives <= 0:
            print("You lost! ")
            continue_game = False
    return remaining_lives, continue_game

numbers = [i for i in range(1, 101)]
picked_number = random.choice(numbers)
remaining_lives = 10
continue_game = True

print("Welcome to the Number Guessing Game! ")
print("I'm thinking about a number between 1 and 100. ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
    remaining_lives = 5

while continue_game:
    remaining_lives, continue_game = count_attempts(remaining_lives, continue_game)
