days_count = int(input())
liters = 0
degrees = 0

for day in range(days_count):
    rakia_quantity = float(input())
    rakia_degree = float(input())
    liters += rakia_quantity
    degrees += rakia_quantity * rakia_degree

print(f'Liter: {liters:.2f}')
print(f'Degrees: {(degrees / liters):.2f}')

if (degrees / liters) < 38:
    print("Not good, you should baking!")
elif 38 <= (degrees / liters) <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")

