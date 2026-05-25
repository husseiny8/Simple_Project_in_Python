# imports
import random
import sys

User_Choices = ["Rock", "Paper", "Scissors"]


# creat function to get user input
def user_input():
    input_user = None
    while input_user not in User_Choices:
        input_user = input("Rock, Paper, Scissors? " + "Or Quit? ")
        if input_user == "Quit":
            sys.exit()
    return input_user


# creat function to get PC input
def computer_choice():
    computer_choice = random.choice(User_Choices)
    return computer_choice

# compare and ...
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("PC Choice:" + computer_choice)
        print("Draw")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("PC Choice:" + computer_choice)
        print("You win")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("PC Choice:" + computer_choice)
        print("You win")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("PC Choice:" + computer_choice)
        print("You win")
    elif user_choice == "Scissors" and computer_choice == "Rock":
        print("PC Choice:" + computer_choice)
        print("PC win")
    elif user_choice == "Paper" and computer_choice == "Scissors":
        print("PC Choice:" + computer_choice)
        print("PC win")
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("PC Choice:" + computer_choice)
        print("PC win")

# crate the main function
def main():
    while True:
        my_input = user_input()
        pc_input = computer_choice()
        determine_winner(my_input, pc_input)

main()
