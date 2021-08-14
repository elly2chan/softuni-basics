budget = float(input())
product_counter = 0
money_spent = 0
money_left = budget
command = input()

while command != "Stop":
    product_price = float(input())
    product_counter += 1
    if product_counter % 3 == 0:
        money_spent += product_price * 0.5
    else:
        money_spent += product_price

    if product_price > money_left:
        break
    command = input()

if money_spent > money_left:
    money_needed = money_spent - money_left
    print("You don't have enough money!")
    print(f'You need {money_needed:.2f} leva more!')
else:
    print(f'You bought {product_counter} products for {money_spent:.2f} leva.')