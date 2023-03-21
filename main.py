import random

player_user = 0
player_computer = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        player_user += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        player_user += 1 

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        player_user += 1


    else:
        print("You lost!")
        player_computer += 1    

print("You won", player_user, "times.")
print("Computer won", player_computer, "times.")
print("Goodbye!")
