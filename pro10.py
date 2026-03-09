import random
import time

print("Memory Number Game")

score = 0
rounds = int(input("Enter number of rounds: "))

for i in range(rounds):
    print("\nRound", i+1)

    numbers = []

    for j in range(4):
        num = random.randint(1, 9)
        numbers.append(num)

    print("Remember these numbers:", numbers)

    time.sleep(3)

    print("\n" * 30)

    guess = input("Enter the numbers separated by space: ")

    user_numbers = list(map(int, guess.split()))

    if user_numbers == numbers:
        print("Correct memory")
        score += 1
    else:
        print("Wrong")
        print("Correct numbers were:", numbers)

    print("Score:", score)

print("\nGame Over")
print("Final Score:", score)