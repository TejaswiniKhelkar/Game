import random

print("Treasure Hunt Game")

treasure = random.randint(1, 20)

attempts = 5
found = False

print("Treasure is hidden between numbers 1 to 20")

for i in range(attempts):
    guess = int(input("Enter a number: "))

    if guess == treasure:
        print("You found the treasure")
        found = True
        break

    elif guess < treasure:
        print("Treasure is at a higher number")

    else:
        print("Treasure is at a lower number")

    print("Attempts left:", attempts - i - 1)

if not found:
    print("You lost the game")
    print("Treasure was at:", treasure)

print("Game Over")