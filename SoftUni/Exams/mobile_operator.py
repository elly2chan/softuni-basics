contract_duration = input()
contract_type = input()
ethernet = input()
months_for_payment = int(input())
price = 0

if contract_duration == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    elif contract_type == "ExtraLarge":
        price = 35.99
    if ethernet == "yes":
        if price <= 10:
            price += 5.50
        elif 10 < price <= 30:
            price += 4.35
        elif price > 30:
            price += 3.85
    price *= months_for_payment
    print(f'{price:.2f} lv.')

elif contract_duration == "two":
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79
    if ethernet == "yes":
        if price <= 10:
            price += 5.50
        elif 10 < price <= 30:
            price += 4.35
        elif price > 30:
            price += 3.85
    price -= price * 3.75 / 100
    price *= months_for_payment
    print(f'{price:.2f} lv.')

