from math import floor

year_type = input()
holidays = int(input())
home_travel_weekends_count = int(input())
weekends = 48
result = 0

if year_type in ("normal", "leap"):
    weekends_in_sofia = weekends - home_travel_weekends_count
    weekends_in_sofia = weekends_in_sofia * 0.75
    volleyball_in_sofia = weekends_in_sofia + (holidays * 2 / 3)
    result = home_travel_weekends_count + volleyball_in_sofia
    if year_type == "leap":
        result = result + (result * 15/ 100)

print(floor(result))



