nylon_sq_meters = int(input())
paint_liters = int(input())
thinner_liters = int(input())
job_hours = int(input())

nylon = nylon_sq_meters + 2
paint = paint_liters + (paint_liters * 10 / 100)

expenses = nylon * 1.50 + paint * 14.50 + thinner_liters * 5.00 + 0.40
job_expenses = (expenses * 30 / 100) * job_hours

print(f'Total expenses: {(expenses + job_expenses):.2f} lv.')