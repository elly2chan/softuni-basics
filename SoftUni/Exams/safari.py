budget = float(input())
gas_needed = float(input())
weekend_day = input()

gas_price = gas_needed * 2.10
guide = 100
total = guide + gas_price

if weekend_day == "Saturday":
    total -= total * 10 / 100
elif weekend_day == "Sunday":
    total -= total * 20 / 100

if budget > total:
    money_left = budget - total
    print(f'Safari time! Money left: {money_left:.2f} lv.')
else:
    money_needed = total - budget
    print(f'Not enough money! Money needed: {money_needed:.2f} lv.')