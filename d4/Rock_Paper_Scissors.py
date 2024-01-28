import random

rock = "ROCK SOLID"
paper = "WEAK PAPER"
scissors = "ME CUT ME SCISSORS"



user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_choice == 0:
    print("User chose Rock", rock)
elif user_choice == 1:
    print("User chose Paper", paper)
elif user_choice == 2:
    print("User chose", scissors)

computer_choice = random.randint(0,2)

if computer_choice == 0:
    print("Computer chose Rock", rock)
elif computer_choice == 1:
    print("Computer chose Paper", paper)
elif computer_choice == 2:
    print("Computer chose", scissors)


# print(f"Computer chose {computer_choice}")

if user_choice == 0:
    if computer_choice == 0:
        print("It's a draw!")
    elif computer_choice == 2:
        print("You Win!")
    else:
        print("You Lose!")
    
if user_choice == 1:
    if computer_choice == 0:
        print("You Won!")
    elif computer_choice == 1:
        print("It's a draw!")
    else:
        print("You Lost!")

if user_choice == 2:
    if computer_choice == 1:
        print("You Won!")
    elif computer_choice == 2:
        print("You Won!")
    else: 
        print("You Lost!")