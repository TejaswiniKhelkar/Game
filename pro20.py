print("Restaurant Order System")

menu = {
    "pizza": 200,
    "burger": 120,
    "pasta": 150,
    "sandwich": 100
}

total = 0

while True:
    print("\nMenu:")
    for item, price in menu.items():
        print(item, "-", price)

    order = input("Enter item to order (or 'done'): ")

    if order == "done":
        break

    if order in menu:
        qty = int(input("Enter quantity: "))
        cost = menu[order] * qty
        total += cost
        print("Added. Cost:", cost)
    else:
        print("Item not available")

print("\nTotal Bill:", total)
print("Thank you for ordering")