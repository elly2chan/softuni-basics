expected_profit = int(input())
service_type = input()
profit = 0

while service_type != "closed":
    if service_type == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            profit += 15
        elif haircut_type == "ladies":
            profit += 20
        elif haircut_type == "kids":
            profit += 10
    elif service_type == "color":
        color_type = input()
        if color_type == "touch up":
            profit += 20
        elif color_type == "full color":
            profit += 30

    if profit >= expected_profit:
        print('You have reached your target for the day!')
        break

    service_type = input()

if profit < expected_profit:
    print(f'Target not reached! You need {expected_profit - profit}lv. more.')

print(f'Earned money: {profit}lv.')