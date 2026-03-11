import random

print("Even Odd Challenge Game")

score = 0
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    print("\nRound", i+1)

    guess = input("Enter even or odd: ").lower()

    number = random.randint(1,20)

    print("Number generated:", number)

    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"

    if guess == result:
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print("Score:", score)

print("\nGame Over")
print("Final Score:", score)