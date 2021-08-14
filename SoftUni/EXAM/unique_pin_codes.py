first_number_end = int(input())
second_number_end = int(input())
third_number_end = int(input())

for a in range(2, first_number_end + 1, 2):
    for b in range(2, second_number_end + 1):
        for c in range(2, third_number_end + 1, 2):
            if b in (2, 3, 5, 7):
                print(f"{a} {b} {c}")