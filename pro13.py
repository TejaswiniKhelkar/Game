import random

print("Guess the Colour Game")

colors = ["red", "blue", "green", "yellow", "purple"]

score = 0
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    color = random.choice(colors)

    print("\nRound", i+1)

    hint = color[0] + "____"
    print("Hint:", hint)

    guess = input("Guess the colour: ").lower()

    if guess == color:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct colour:", color)

    print("Score:", score)

print("\nGame Over")
print("Final Score:", score)