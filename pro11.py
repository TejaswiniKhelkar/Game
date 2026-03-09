print("Word Chain Game")

rounds = int(input("Enter number of rounds: "))
score = 0

word = input("Enter starting word: ")

for i in range(rounds):
    print("\nCurrent word:", word)

    next_word = input("Enter a word starting with '" + word[-1] + "': ")

    if next_word[0].lower() == word[-1].lower():
        print("Correct word")
        score += 1
        word = next_word
    else:
        print("Wrong word")
        print("Word should start with:", word[-1])
        break

    print("Score:", score)

print("\nGame Over")
print("Final Score:", score)

if score == rounds:
    print("Excellent")
elif score > 0:
    print("Good try")
else:
    print("Better luck next time")