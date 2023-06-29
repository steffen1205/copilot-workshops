# write a rock, paper, scissors game
# 1. get the user input
# 2. get the computer input
# 3. compare the inputs
# 4. print the results
# import random module
import random
# define main function that handles the game
def main():
    options = ["rock", "paper", "scissors"]

    # Get the user input and convert it to lowercase
    user = input("Rock, paper, or scissors? ").lower()
    while user not in options:
        print("Invalid input. Please choose rock, paper, or scissors.")
        user = input("Rock, paper, or scissors? ").lower()

    # Get the computer input
    computer = random.choice(options)

    # Print the choices made by the user and the computer
    print("You chose:", user)
    print("Computer chose:", computer)

    # Compare the inputs
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

# Call the main function
main()
