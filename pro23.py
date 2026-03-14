print("Expense Tracker")

expenses = []
total = 0

while True:
    print("\n1 Add Expense")
    print("2 View Expenses")
    print("3 Total Expense")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((item, amount))
        print("Expense added")

    elif choice == "2":
        for item, amount in expenses:
            print(item, ":", amount)

    elif choice == "3":
        total = 0
        for item, amount in expenses:
            total += amount
        print("Total Expense:", total)

    elif choice == "4":
        print("Exiting tracker")
        break

    else:
        print("Invalid choice")