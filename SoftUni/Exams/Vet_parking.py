days = int(input())
hours = int(input())
parking = 0

for day in range(1, days + 1):
    day_parking = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            day_parking += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            day_parking += 1.25
        else:
            day_parking += 1
    print(f'Day: {day} - {day_parking:.2f} leva')
    parking += day_parking
print(f'Total: {parking:.2f} leva')