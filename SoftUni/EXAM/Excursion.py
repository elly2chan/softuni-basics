people_count = int(input())
nights_count = int(input())
transport_cards_count = int(input())
museum_tickets_count = int(input())

nights = (nights_count * 20) * people_count
transport_cards = (transport_cards_count * 1.60) * people_count
museum_tickets = (museum_tickets_count * 6) * people_count

total = nights + transport_cards + museum_tickets
total += total * 25 / 100

print(f'{total:.2f}')