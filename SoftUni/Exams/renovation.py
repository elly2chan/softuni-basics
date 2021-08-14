from math import ceil

wall_height = int(input())
wall_width = int(input())
occupied_space_perc = int(input())
paint_bought = int(input())

walls = wall_height * wall_width * 4
paint_area = ceil(walls - (walls * occupied_space_perc / 100))
paint_used = 0

while paint_bought != "Tired!":
    paint_used += int(paint_bought)
    if paint_used > paint_area:
        break
    elif paint_used == paint_area:
        break
    paint_bought = input()

if paint_used > paint_area:
    print(f'All walls are painted and you have {paint_used - paint_area} l paint left!')
elif paint_used == paint_area:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f'{paint_area - paint_used} quadratic m left.')
