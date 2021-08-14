drink_type = input()
sugar = input()
drink_counter = int(input())

if sugar == "Without":
    if drink_type == "Espresso":
        price = 0.90
    elif drink_type == "Cappuccino":
        price = 1
    elif drink_type == "Tea":
        price = 0.50

elif sugar == "Normal":
    if drink_type == "Espresso":
        price = 1
    elif drink_type == "Cappuccino":
        price = 1.20
    elif drink_type == "Tea":
        price = 0.60

elif sugar == "Extra":
    if drink_type == "Espresso":
        price = 1.20
    elif drink_type == "Cappuccino":
        price = 1.60
    elif drink_type == "Tea":
        price = 0.70

price *= drink_counter

if sugar == "Without":
    price -= price * 0.35

if drink_type == "Espresso":
    if drink_counter >= 5:
        price -= price * 0.25

if price > 15:
    price -= price * 0.2

print(f'You bought {drink_counter} cups of {drink_type} for {price:.2f} lv.')