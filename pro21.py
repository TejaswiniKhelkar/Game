print("Library Book Management System")

books = []

while True:
    print("\n1 Add Book")
    print("2 View Books")
    print("3 Remove Book")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added")

    elif choice == "2":
        if len(books) == 0:
            print("No books available")
        else:
            print("Book List:")
            for b in books:
                print(b)

    elif choice == "3":
        remove = input("Enter book name to remove: ")
        if remove in books:
            books.remove(remove)
            print("Book removed")
        else:
            print("Book not found")

    elif choice == "4":
        print("Exiting system")
        break

    else:
        print("Invalid choice")