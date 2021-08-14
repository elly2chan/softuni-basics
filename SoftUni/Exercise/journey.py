budget = float(input())
season = input()
destination = ""
place_to_stay = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_to_stay = "Camp"
        money_spent = budget * 30 / 100
    elif season == "winter":
        place_to_stay = "Hotel"
        money_spent = budget * 70 / 100
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place_to_stay = "Camp"
        money_spent = budget * 40 / 100
    elif season == "winter":
        place_to_stay = "Hotel"
        money_spent = budget * 80 / 100
elif budget > 1000:
    destination = "Europe"
    place_to_stay = "Hotel"
    money_spent = budget * 90 / 100

print(f'Somewhere in {destination}')
print(f'{place_to_stay} - {money_spent:.2f}')


