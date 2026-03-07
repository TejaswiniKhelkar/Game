import random

print("Dice Rolling Game")

user_score = 0
computer_score = 0

rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    input("Press Enter to roll the dice")

    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("You rolled:", user_roll)
    print("Computer rolled:", computer_roll)

    if user_roll > computer_roll:
        print("You win this round")
        user_score += 1

    elif computer_roll > user_roll:
        print("Computer wins this round")
        computer_score += 1

    else:
        print("Round Draw")

    print("Score -> You:", user_score, "Computer:", computer_score)
    print()

print("Final Score")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("You won the game")
elif computer_score > user_score:
    print("Computer won the game")
else:
    print("Game Draw")