print("Shopping List Manager")

shopping_list = []

while True:
    print("\n1 Add Item")
    print("2 Remove Item")
    print("3 View List")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print("Item added")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    elif choice == "3":
        print("Shopping List:", shopping_list)

    elif choice == "4":
        break