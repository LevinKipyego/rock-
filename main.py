import random

while 1:
    user= input("Enter a choice (r,p,s): ")
    actions = ["r", "p", "s"]
    cpu= random.choice(actions)
    print(f"\nYou chose {user}, computer chose {cpu}.\n")

    if user == cpu:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "r":
        if cpu == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "p":
        if cpu== "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if cpu  == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
    	print(f"you chose {user_action} an invalid option please check and choose perfectly")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break