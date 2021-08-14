projection_type = input()
rows_count = int(input())
columns_count = int(input())
income = 0

if projection_type == "Premiere":
    income = rows_count * columns_count * 12
elif projection_type == "Normal":
    income = rows_count * columns_count * 7.50
elif projection_type == "Discount":
    income = rows_count * columns_count * 5

print(f'{income:.2f} leva')