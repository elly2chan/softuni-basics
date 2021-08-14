movie = input()
cinema_hall_type = input()
tickets_quantity = int(input())
ticket_price = 0
profit = 0

if movie == "A Star Is Born":
    if cinema_hall_type == "normal":
        ticket_price = 7.50
    elif cinema_hall_type == "luxury":
        ticket_price = 10.50
    elif cinema_hall_type == "ultra luxury":
        ticket_price = 13.50

elif movie == "Bohemian Rhapsody":
    if cinema_hall_type == "normal":
        ticket_price = 7.35
    elif cinema_hall_type == "luxury":
        ticket_price = 9.45
    elif cinema_hall_type == "ultra luxury":
        ticket_price = 12.75

elif movie == "Green Book":
    if cinema_hall_type == "normal":
        ticket_price = 8.15
    elif cinema_hall_type == "luxury":
        ticket_price = 10.25
    elif cinema_hall_type == "ultra luxury":
        ticket_price = 13.25

elif movie == "The Favourite":
    if cinema_hall_type == "normal":
        ticket_price = 8.75
    elif cinema_hall_type == "luxury":
        ticket_price = 11.55
    elif cinema_hall_type == "ultra luxury":
        ticket_price = 13.95

profit = ticket_price * tickets_quantity

print(f'{movie} -> {profit:.2f} lv.')