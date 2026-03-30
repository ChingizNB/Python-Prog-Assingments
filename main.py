# Task D1 - Multiple Orders (while loop)
customer_name = input("Enter customer name: ")
subtotal = 0.0
item_count = 0

while True:
    item_name = input("Enter item name (or 'done' to finish): ")

    if item_name.lower() == 'done':
        break

    price = float(input("Enter price: "))
    subtotal += price
    item_count += 1

print(f"\nCustomer: {customer_name.upper()}")
print(f"Items: {item_count}")
print(f"Subtotal {subtotal} KZT")

# Task D2 - Time-Based Discount (if/elif/else)
hour = int(input("\nEnter current hour (0-23): "))

if 6 <= hour < 12:
    discount_label = "Morning discount"
    discount_percent = 0.10  # 10% off
elif 12 <= hour < 17:
    discount_label = "No discount"
    discount_percent = 0.0
elif 17 <= hour < 22:
    discount_label = "Evening discount"
    discount_percent = 0.05  # 5% off
else:
    print("Closed")
    discount_label = None

if discount_label is not None:
    discount_amount = subtotal * discount_percent
    discounted_price = subtotal - discount_amount
    tip = discounted_price * 0.10
    total = discounted_price + tip

    print(f"Time period: {discount_label}")
    print(f"Discount: {discount_amount} KZT")
    print(f"Tip (10%): {tip} KZT")
    print(f"Total: {total} KZT")

# Task D3 - Name Analysis (strings)
print(f"\nName uppercase: {customer_name.upper()}")
print(f"Name lowercase: {customer_name.lower()}")
print(f"Name length: {len(customer_name)}")

if customer_name[0].upper() == 'A' or customer_name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")