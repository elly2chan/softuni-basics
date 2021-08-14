budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_total = video_cards * 250
processors_total = (video_cards_total * 35 / 100) * processors
ram_memory_total = (video_cards_total * 10 / 100) * ram_memory

total = video_cards_total + processors_total + ram_memory_total

if video_cards > processors:
    total -= total * 15 / 100

if budget >= total:
    money_left = budget - total
    print(f'You have {money_left:.2f} leva left!')
else:
    money_needed = total - budget
    print(f'Not enough money! You need {money_needed:.2f} leva more!')
