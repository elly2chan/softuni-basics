numbers_quantity = int(input())
counter = 0
p1 = 0
p2 = 0
p3 = 0

while counter < numbers_quantity:
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

    counter += 1

p1 = p1 / numbers_quantity * 100
p2 = p2 / numbers_quantity * 100
p3 = p3 / numbers_quantity * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')