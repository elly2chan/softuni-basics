from math import ceil
from math import floor

absent_days_count = int(input())
food_available = int(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())

food_eaten = (first_deer_food_per_day * absent_days_count) + (second_deer_food_per_day * absent_days_count) \
    + (third_deer_food_per_day * absent_days_count)

if food_available >= food_eaten:
    print(f'{floor(food_available - food_eaten)} kilos of food left.')
else:
    print(f'{ceil(food_eaten - food_available)} more kilos of food needed.')