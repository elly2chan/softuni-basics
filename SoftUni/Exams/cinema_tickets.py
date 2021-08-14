student_tickets = 0
standard_tickets = 0
kid_tickets = 0
tickets_sold = 0

while True:
    movie = input()
    if movie == "Finish":
        break
    capacity = int(input())
    tickets_sold = 0

    while capacity > tickets_sold:
        ticket_type = input()
        if ticket_type == "End":
            print('\n')
            break

        tickets_sold += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

    print(f'{movie} - {tickets_sold / capacity * 100:.2f}% full.')
tickets_counter = student_tickets + standard_tickets + kid_tickets
print(f'Total tickets: {tickets_counter}')
print(f'{student_tickets / tickets_counter * 100:.2f}% student tickets.')
print(f'{standard_tickets / tickets_counter * 100:.2f}% standard tickets.')
print(f'{kid_tickets / tickets_counter * 100:.2f}% kids tickets.')
