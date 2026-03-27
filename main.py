# a) Ввод данных [cite: 170, 171]
customer = input("Enter customer name: ")
item1 = input("Enter name of item 1: ")
price1 = float(input("Enter price of item 1 (KZT): "))
item2 = input("Enter name of item 2: ")
price2 = float(input("Enter price of item 2 (KZT): "))
people = int(input("Enter number of people: "))

# b) Расчеты [cite: 180, 181]
subtotal = price1 + price2 # [cite: 182]
tip = subtotal * 0.10 # [cite: 183]
total = subtotal + tip # [cite: 184]
per_person = total / people # [cite: 185]

# c) Вывод чека [cite: 186, 187]
print("=" * 30) # [cite: 201]
print("CAFE BILL")
print("-" * 30)
print(f"Customer: {customer}")
print(f"{item1}: {price1} KZT")
print(f"{item2}: {price2} KZT")
print(f"Subtotal: {subtotal} KZT")
print(f"Tip (10%): {tip} KZT")
print(f"Total: {total} KZT")
print(f"Per person: {per_person} KZT")
print("=" * 30)

# d) Сравнение [cite: 202, 203]
print("Tip included:", tip > 0) # [cite: 204, 206]
print("Bill over 5000 KZT:", total > 5000) # [cite: 205]