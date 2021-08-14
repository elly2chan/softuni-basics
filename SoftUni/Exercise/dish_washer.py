bottles_count = int(input())
detergent_amount = bottles_count * 750
dishes_count = input()
counter = 1
dishes = 0
pots = 0

while dishes_count != "End":
    dishes_count = int(dishes_count)
    if counter < 3:
        detergent_amount -= dishes_count * 5
        dishes += dishes_count
        counter += 1
    else:
        detergent_amount -= dishes_count * 15
        pots += dishes_count
        counter = 1

    if detergent_amount < 0:
        print(f'Not enough detergent, {abs(detergent_amount)} ml. more necessary!')
        break

    dishes_count = input()

if detergent_amount >= 0:
    print('Detergent was enough!')
    print(f'{dishes} dishes and {pots} pots were washed.')
    print(f'Leftover detergent, {detergent_amount} ml.')
