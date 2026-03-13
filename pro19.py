print("Contact List Manager")

contacts = {}

while True:
    print("\n1 Add Contact")
    print("2 View Contacts")
    print("3 Search Contact")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added")

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(search, ":", contacts[search])
        else:
            print("Contact not found")

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid choice")