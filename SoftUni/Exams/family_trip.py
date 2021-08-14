budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_expenses_perc = int(input())

sleep = nights * price_per_night
additional_expenses = budget * additional_expenses_perc / 100

if nights > 7:
    sleep -= sleep * 5 / 100

total = sleep + additional_expenses

if budget >= total:
    money_left = budget - total
    print(f'Ivanovi will be left with {money_left:.2f} leva after vacation.')
else:
    money_needed = total - budget
    print(f'{money_needed:.2f} leva needed.')