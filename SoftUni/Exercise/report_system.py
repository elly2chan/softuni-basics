expected_profit = int(input())
product_price = input()
counter = 1
cash_payments = 0
cash_amount = 0
card_payments = 0
card_amount = 0
money_raised = 0

while product_price != "End":
    product_price = int(product_price)
    if counter % 2 != 0:
        if product_price > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            cash_payments += 1
            cash_amount += product_price
            money_raised += product_price
        counter += 1
    else:
        if product_price < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            card_payments += 1
            card_amount += product_price
            money_raised += product_price
        counter += 1

    if money_raised >= expected_profit:
        print(f'Average CS: {(cash_amount / cash_payments):.2f}')
        print(f'Average CC: {(card_amount / card_payments):.2f}')
        break

    product_price = input()

if money_raised < expected_profit:
    print('Failed to collect required money for charity.')
