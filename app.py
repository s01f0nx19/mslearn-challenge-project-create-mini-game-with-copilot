#create a python mini game rock-paper-scissors, where  player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent
#By the end of each round, the player can choose whether to play again
#Display the player's score at the end of the game
#The mini game must handle user inputs, putting them in lowercase and informing the user if the option is invalid
rock = "rock"
paper = "paper"
scissors = "scissors"
player_score = 0
computer_score = 0
while True:
    player = input("Enter rock, paper, or scissors: ").lower()
    if player == rock or player == paper or player == scissors:
        import random
        computer = random.choice([rock, paper, scissors])
        print(f"Computer chose {computer}")
        if player == computer:
            print("It's a tie!")
        elif player == rock and computer == scissors:
            print("You win!")
            player_score += 1
        elif player == paper and computer == rock:
            print("You win!")
            player_score += 1
        elif player == scissors and computer == paper:
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1
        print(f"Player: {player_score} Computer: {computer_score}")
    else:
        print("Invalid option!")
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        break
print("Game over!")

