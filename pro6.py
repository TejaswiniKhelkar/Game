import random

print("Math Quiz Game")

score = 0
rounds = int(input("Enter number of questions: "))

for i in range(rounds):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    op = random.choice(["+", "-", "*"])

    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    print("\nQuestion", i+1)
    user = int(input(f"{num1} {op} {num2} = "))

    if user == answer:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct answer:", answer)

    print("Score:", score)

print("\nGame Over")
print("Final Score:", score)

if score == rounds:
    print("Excellent")
elif score >= rounds//2:
    print("Good job")
else:
    print("Practice more")