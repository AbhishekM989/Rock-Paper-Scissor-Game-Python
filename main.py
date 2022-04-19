import random

while True:

    user_action = input("Enter Your Choice (Rock, Paper, Scissor): ")

    possible_actions = ["Rock", "Paper", "Scissor"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou Chose {user_action}, Computer Chose {computer_action}. \n")


    if user_action == computer_action:
        print(f"Both Players Selected {user_action} It's A Tie!")

    elif user_action == "Rock":
        if computer_action == "Scissor":
            print(f"Rock Smashes Scissor ! You Win !")

        else:
            print(f"Paper Covers Rock You Lose !")


    elif user_action == "Paper":
        if computer_action == "Rock":
            print(f"Paper Cover Rock You Lose !")

        else:
            print('Scissor Cuts Paper You Win !')

    elif user_action == "Scissor":
        if computer_action == "Paper":
            print("Scissor Cuts Paper You Win !")

        else:
            print("Rock Smashes Scissor You Lose !")        


    play_again = input("Do You Want To Play Again ? (y/n):")
    if play_again.lower() != "y":
        break    