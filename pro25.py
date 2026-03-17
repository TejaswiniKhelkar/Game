print("Password Manager")

data = {}

while True:
    print("\n1 Add Password")
    print("2 View All")
    print("3 Search Account")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        account = input("Enter account name: ")
        password = input("Enter password: ")
        data[account] = password
        print("Saved successfully")

    elif choice == "2":
        if len(data) == 0:
            print("No data stored")
        else:
            for acc, pwd in data.items():
                print(acc, ":", pwd)

    elif choice == "3":
        acc = input("Enter account to search: ")
        if acc in data:
            print("Password:", data[acc])
        else:
            print("Account not found")

    elif choice == "4":
        print("Exiting manager")
        break

    else:
        print("Invalid choice")