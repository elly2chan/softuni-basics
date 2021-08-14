expected_profit = float(input())
cocktail_name = input()
profit = 0

while cocktail_name != "Party!":

    current_order = 0
    cocktail_quantity = int(input())
    price = len(cocktail_name)
    current_order = price * cocktail_quantity

    if current_order % 2 != 0:
        current_order -= current_order * 25 / 100
        profit += current_order
    else:
        profit += current_order

    if profit >= expected_profit:
        break

    cocktail_name = input()

if profit >= expected_profit:
    print("Target acquired.")
else:
    print(f'We need {(expected_profit - profit):.2f} leva more.')

print(f'Club income - {profit:.2f} leva.')

