stay = int(input())
room_type = input()
feedback = input()
price = 0

if stay < 10:
    if room_type == "room for one person":
        price = 18 * (stay - 1)
    elif room_type == "apartment":
        price = 25 * (stay - 1)
        discount = price * 30 / 100
        price -= discount
    elif room_type == "president apartment":
        price = 35 * (stay - 1)
        discount = price * 10 / 100
        price -= discount
elif 10 <= stay <= 15:
    if room_type == "room for one person":
        price = 18 * (stay - 1)
    elif room_type == "apartment":
        price = 25 * (stay - 1)
        discount = price * 35 / 100
        price -= discount
    elif room_type == "president apartment":
        price = 35 * (stay - 1)
        discount = price * 15 / 100
        price -= discount
elif stay > 15:
    if room_type == "room for one person":
        price = 18 * (stay - 1)
    elif room_type == "apartment":
        price = 25 * (stay - 1)
        discount = price / 2
        price -= discount
    elif room_type == "president apartment":
        price = 35 * (stay - 1)
        discount = price * 20 / 100
        price -= discount

if feedback == "positive":
    price = price + (price * 25 / 100)
    print(f'{price:.2f}')
elif feedback == "negative":
    price = price - (price * 10 / 100)
    print(f'{price:.2f}')