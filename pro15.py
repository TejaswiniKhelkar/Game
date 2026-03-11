import random

print("Word Length Guess Game")

words = ["python", "keyboard", "science", "internet", "computer", "program"]

score = 0
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    word = random.choice(words)

    print("\nRound", i+1)

    print("Word hint:", word[0] + "..." + word[-1])

    guess = int(input("Guess the length of the word: "))

    length = len(word)

    print("Actual length:", length)

    if guess == length:
        print("Correct guess")
        score += 2

    elif abs(guess - length) == 1:
        print("Very close")
        score += 1

    else:
        print("Wrong guess")

    print("Score:", score)

print("\nGame Over")
print("Final Score:", score)

if score >= rounds*2:
    print("Excellent")
elif score >= rounds:
    print("Good job")
else:
    print("Try again")