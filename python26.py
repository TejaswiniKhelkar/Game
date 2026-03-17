print("Parking Lot Manager")

total_slots = 5
available = total_slots

while True:
    print("\nTotal Slots:", total_slots)
    print("Available Slots:", available)
    print("1 Park Car")
    print("2 Remove Car")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if available > 0:
            car = input("Enter car number: ")
            available -= 1
            print("Car parked:", car)
        else:
            print("Parking full")

    elif choice == "2":
        if available < total_slots:
            car = input("Enter car number to remove: ")
            available += 1
            print("Car removed:", car)
        else:
            print("Parking already empty")

    elif choice == "3":
        print("Exiting system")
        break

    else:
        print("Invalid choice")
