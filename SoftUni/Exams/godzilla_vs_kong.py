budget = float(input())
extras = int(input())
costume_price = float(input())

decor = budget * 10 / 100
costumes = extras * costume_price

if extras > 150:
    costumes -= costumes * 10 / 100

if budget < (decor + costumes):
    money_needed = (decor + costumes) - budget
    print("Not enough money!")
    print(f'Wingard needs {money_needed:.2f} leva more.')
else:
    money_left = budget - (decor + costumes)
    print("Action!")
    print(f'Wingard starts filming with {money_left:.2f} leva left.')