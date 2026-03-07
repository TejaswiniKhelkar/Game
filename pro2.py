import random

print("Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    print("\nRound", i+1)

    user = input("Enter rock, paper or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Draw")

    elif user == "rock" and computer == "scissors":
        print("You win this round")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You win this round")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You win this round")
        user_score += 1

    else:
        print("Computer wins this round")
        computer_score += 1

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("You won the game")
elif computer_score > user_score:
    print("Computer won the game")
else:
    print("Game Draw")
