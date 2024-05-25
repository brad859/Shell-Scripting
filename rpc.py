import random

while True: 
    user_action = input("Type (rock, paper, scissors): ")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. tie game!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You are the champ!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You are the champ!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print('Scissors cuts paper! You are the champ!')
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (yes / no): ")
    if play_again.lower() != "yes":
        break