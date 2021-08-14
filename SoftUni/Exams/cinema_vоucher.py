voucher_sum = int(input())
purchase_price = 0
money_left = voucher_sum
tickets_counter = 0
others_counter = 0

while True:

    purchase = input()

    if purchase == "End":
        print(f'{tickets_counter}')
        print(f'{others_counter}')
        break

    if len(purchase) > 8:
        purchase_price = (ord(purchase[0]) + ord(purchase[1]))
        print(purchase_price)
        if purchase_price > money_left:
            print(f'{tickets_counter}')
            print(f'{others_counter}')
            break
        else:
            tickets_counter += 1

    elif len(purchase) <= 8:
        purchase_price = ord(purchase[0])
        print(purchase_price)
        if purchase_price > money_left:
            print(f'{tickets_counter}')
            print(f'{others_counter}')
            break
        else:
            others_counter += 1

    money_left -= purchase_price