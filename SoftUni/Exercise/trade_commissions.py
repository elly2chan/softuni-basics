city = input()
sales = float(input())
commission = 0

if sales < 0:
    print("error")
else:
    if city == "Sofia":
        if 0 <= sales <= 500:
            commission = sales * 5 / 100
        elif 500 < sales <= 1000:
            commission = sales * 7 / 100
        elif 1000 < sales <= 10000:
            commission = sales * 8 / 100
        else:
            commission = sales * 12 / 100
    elif city == "Varna":
        if 0 <= sales <= 500:
            commission = sales * 4.5 / 100
        elif 500 < sales <= 1000:
            commission = sales * 7.5 / 100
        elif 1000 < sales <= 10000:
            commission = sales * 10 / 100
        else:
            commission = sales * 13 / 100
    elif city == "Plovdiv":
        if 0 <= sales <= 500:
            commission = sales * 5.5 / 100
        elif 500 < sales <= 1000:
            commission = sales * 8 / 100
        elif 1000 < sales <= 10000:
            commission = sales * 12 / 100
        else:
            commission = sales * 14.5 / 100
    else:
        print("error")

if commission > 0:
    print(f'{commission:.2f}')
