budget = int(input())
season = input()
fishermen = int(input())
price = 0

if season == "Spring":
    price = 3000
    if fishermen % 2 == 0:
        price = price - (price * 5 / 100)
elif season in ("Summer", "Autumn"):
    price = 4200
    if fishermen % 2 == 0 and season != "Autumn":
        price = price - (price * 5 / 100)
elif season == "Winter":
    price = 2600
    if fishermen % 2 == 0:
        price = price - (price * 5 / 100)

if fishermen <= 6:
    price = price - (price * 10 / 100)
elif 7 <= fishermen <= 11:
    price = price - (price * 15 / 100)
elif fishermen >= 12:
    price = price - (price * 25 / 100)

if budget >= price:
    money_left = budget - price
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = price - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')


