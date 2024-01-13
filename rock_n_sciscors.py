import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
players = input("Choose from the option below:\n"
                "1. Rock\n"
                "2. Paper\n"
                "3. Scissors\n")

if players.isdigit():
    if 1 <= int(players) <= 3:
        print("Player: ", choices[int(players) - 1])
        print("Computer: ", computer)
        if choices[int(players) - 1] == computer:
            print("Tie")

        elif choices[int(players) - 1] == choices[0]:
            if computer == choices[1]:
                print("You loose")
            if computer == choices[2]:
                print("You win")

        elif choices[int(players) - 1] == choices[2]:
            if computer == choices[0]:
                print("You loose")
            if computer == choices[1]:
                print("You win")

        elif choices[int(players) - 1] == choices[1]:
            if computer == choices[2]:
                print("You loose")
            if computer == choices[0]:
                print("You win")

    else:
        print("Please select a valid option")
else:
    print("You have to select a number")

