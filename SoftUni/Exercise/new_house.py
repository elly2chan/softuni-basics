flowers_type = input()
flowers_count = int(input())
budget = int(input())
bill = 0

if flowers_type == "Roses":
    bill = flowers_count * 5
    if flowers_count > 80:
        bill = bill - (bill * 10 / 100)
elif flowers_type == "Dahlias":
    bill = flowers_count * 3.80
    if flowers_count > 90:
        bill = bill - (bill * 15 / 100)
elif flowers_type == "Tulips":
    bill = flowers_count * 2.80
    if flowers_count > 80:
        bill = bill - (bill * 15 / 100)
elif flowers_type == "Narcissus":
    bill = flowers_count * 3
    if flowers_count < 120:
        bill = bill + (bill * 15 / 100)
elif flowers_type == "Gladiolus":
    bill = flowers_count * 2.50
    if flowers_count < 80:
        bill = bill + (bill * 20 / 100)

if budget >= bill:
    money_left = budget - bill
    print(f'Hey, you have a great garden with {flowers_count} {flowers_type} and {money_left:.2f} leva left.')
else:
    money_needed = bill - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')