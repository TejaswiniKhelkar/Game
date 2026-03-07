import random

print("Word Scramble Game")

words = ["python", "computer", "science", "program", "keyboard", "internet"]

score = 0
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    word = random.choice(words)

    scrambled = ''.join(random.sample(word, len(word)))

    print("\nRound", i+1)
    print("Unscramble this word:", scrambled)

    guess = input("Your guess: ")

    if guess.lower() == word:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct word was:", word)

    print("Score:", score)

print("\nGame Over")
print("Final Score:", score)

if score == rounds:
    print("Excellent")
elif score >= rounds//2:
    print("Good Job")
else:
    print("Try Again")