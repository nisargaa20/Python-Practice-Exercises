import random

while True:
    user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissor:"))

    if user_choice >= 3 or user_choice < 0:
        print("Invalid")
    else:
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(computer_choice)

        if computer_choice == user_choice:
            print("It's a draw")
        elif (computer_choice == 0 and user_choice == 2) or (user_choice == 0 and computer_choice == 2):
            print("You win")
        elif computer_choice > user_choice:
            print("You lose")
        else:
            print("You win")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
