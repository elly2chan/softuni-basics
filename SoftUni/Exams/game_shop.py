games_quantity = int(input())
counter = games_quantity
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

while counter > 0:
    game = input()
    if game == "Hearthstone":
        hearthstone += 1
    elif game == "Fornite":
        fornite += 1
    elif game == "Overwatch":
        overwatch += 1
    else:
        others += 1
    counter -= 1

print(f'Hearthstone - {(hearthstone / games_quantity * 100):.2f}%')
print(f'Fornite - {(fornite / games_quantity * 100):.2f}%')
print(f'Overwatch - {(overwatch / games_quantity * 100):.2f}%')
print(f'Others - {(others / games_quantity * 100):.2f}%')