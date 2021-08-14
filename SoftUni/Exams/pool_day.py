from math import ceil

people_quantity = int(input())
entrance_fee = float(input())
sunbed_fee = float(input())
umbrella_fee = float(input())

total = 0

umbrellas = ceil(people_quantity * 0.5)
sunbeds = ceil(people_quantity * 0.75)
total = umbrellas * umbrella_fee + sunbeds * sunbed_fee + people_quantity * entrance_fee

print(f'{total:.2f} lv.')
