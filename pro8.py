import random

print("Secret Code Breaker Game")

code = str(random.randint(100, 999))

attempts = 5

print("Guess the 3 digit secret code")

for i in range(attempts):
    guess = input("Enter your guess: ")

    if guess == code:
        print("Correct code")
        print("You unlocked the secret")
        break

    correct = 0

    for j in range(3):
        if guess[j] == code[j]:
            correct += 1

    print("Digits in correct position:", correct)
    print("Attempts left:", attempts - i - 1)

else:
    print("You failed to break the code")
    print("Secret code was:", code)

print("Game Over")