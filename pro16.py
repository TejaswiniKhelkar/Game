print("Simple Billing System")

total = 0

items = int(input("Enter number of items: "))

for i in range(items):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    qty = int(input("Enter quantity: "))

    cost = price * qty
    total += cost

    print("Item:", name, "Cost:", cost)

print("\nTotal Bill:", total)

discount = 0

if total > 500:
    discount = total * 0.1

final = total - discount

print("Discount:", discount)
print("Final Amount:", final)