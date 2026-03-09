import random

print("Guess the Animal Game")

animals = {
    "lion": "King of jungle",
    "elephant": "Largest land animal",
    "tiger": "Striped big cat",
    "giraffe": "Tallest animal",
    "kangaroo": "Animal with pouch"
}

keys = list(animals.keys())

score = 0
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    animal = random.choice(keys)
    hint = animals[animal]

    print("\nRound", i+1)
    print("Hint:", hint)

    guess = input("Guess the animal: ").lower()

    if guess == animal:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct answer:", animal)

    print("Score:", score)

print("\nGame Over")
print("Final Score:", score)

if score == rounds:
    print("Excellent")
elif score >= rounds//2:
    print("Good")
else:
    print("Better luck next time")