print("Movie Ticket Booking System")

seats = 10

while True:
    print("\nAvailable seats:", seats)
    print("1 Book Ticket")
    print("2 Cancel Ticket")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        num = int(input("Enter number of tickets: "))
        if num <= seats:
            seats -= num
            print("Tickets booked")
        else:
            print("Not enough seats")

    elif choice == "2":
        num = int(input("Enter number of tickets to cancel: "))
        seats += num
        print("Tickets cancelled")

    elif choice == "3":
        print("Thank you")
        break

    else:
        print("Invalid choice")