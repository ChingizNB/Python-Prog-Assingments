# Task D1: Сбор данных
from itertools import count

name = input ("Enter customer name:")
subtotal, count= 0.0,0

while True:
    item = input("Enter item(or'done:")
    if item.lower() == 'done': break
    subtotal += float(input("enter price:"))
    count += 1

print(f"n\customer: {name.upper()}\nItems:{count}\nSubtotal {subtotal}KZT")
# Task D2: Скидки и расчеты
hour= int(input("\nEnter current hour(0-23)"))
label,disc = None ,0.0

if 6<= hour < 12: label,disc =  "Morning discount", 0.1
elif 12<= hour < 17:label,disc = 'no discount', 0.0
elif 17<= hour < 22:label,disc = "evening disscount", 0.05
else : print("closed")

if label :
    d_amt= subtotal*disc
    tip=(subtotal -d_amt)* 0.1
    print(f"Time period: {label}\nDiscount:{d_amt} KZT\nTip:{tip}KZT\nTotal:{subtotal -d_amt +tip} KZT")

# Task D3: Анализ имени
print(f"\nName uppercase: {name.upper()}\nName lowercase: {name.lower()}\nName length: {len(name)}")

# Требование: использовать if/else и логический оператор or
if name[0].upper() == 'A' or name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")