import random

print("Lucky Number Game")

score = 0
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    print("\nRound", i+1)

    lucky_number = random.randint(1, 10)

    guess = int(input("Guess the lucky number (1-10): "))

    print("Lucky number was:", lucky_number)

    if guess == lucky_number:
        print("You guessed correctly")
        score += 2

    elif abs(guess - lucky_number) == 1:
        print("Very close")
        score += 1

    else:
        print("Wrong guess")

    print("Current score:", score)

print("\nGame Over")
print("Final Score:", score)

if score >= rounds*2:
    print("Excellent")
elif score >= rounds:
    print("Good")
else:
    print("Try again")