print("Welcome to the Treasure Island. ")
print("Your mission is to find the treasure.")

turn = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n ").lower()
if turn == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n ").lower()
    if lake == "swim":
        print("You drowned. RIP. Game over.")
    else:
        choose_room = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choose_room == "blue":
            print("You enter a room of beasts. RIP, Game Over.")
        elif choose_room == "red":
            print("You set yourself on fire. RIP. Game Over.")
        elif choose_room == "yellow":
            print("You choose the treasury! Good job! You won the game!")
else:
    print("You fall into the deadly trap. Game over")
    
