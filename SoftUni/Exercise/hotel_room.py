month = input()
nights_stay = int(input())
apartment_price = 0
studio_price = 0
whole_stay_studio = 0
whole_stay_apartment = 0

if month in ("May", "October"):
    studio_price = 50
    apartment_price = 65
    whole_stay_studio = nights_stay * studio_price
    whole_stay_apartment = nights_stay * apartment_price
    if 7 < nights_stay <= 14:
        discount = studio_price - studio_price * 5 / 100
        whole_stay_studio = nights_stay * discount
    elif nights_stay > 14:
        discount = studio_price - studio_price * 30 / 100
        whole_stay_studio = nights_stay * discount
        whole_stay_apartment = whole_stay_apartment - (whole_stay_apartment * 10 / 100)

elif month in ("June", "September"):
    studio_price = 75.20
    apartment_price = 68.70
    whole_stay_studio = nights_stay * studio_price
    whole_stay_apartment = nights_stay * apartment_price
    if nights_stay > 14:
        discount = whole_stay_studio * 20 / 100
        whole_stay_studio -= discount
        whole_stay_apartment = whole_stay_apartment - (whole_stay_apartment * 10 / 100)

elif month in ("July", "August"):
    studio_price = 76
    apartment_price = 77
    whole_stay_studio = nights_stay * studio_price
    whole_stay_apartment = nights_stay * apartment_price
    if nights_stay > 14:
        whole_stay_apartment = whole_stay_apartment - (whole_stay_apartment * 10 / 100)

print(f'Apartment: {whole_stay_apartment:.2f} lv.')
print(f'Studio: {whole_stay_studio:.2f} lv.')

