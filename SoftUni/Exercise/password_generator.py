from string import ascii_lowercase

n = int(input())
l = int(input())

for x in range(1, n):
    for y in range(1, n):
        for i in range(0, l):
            for j in range(0, l):
                for h in range(1, n + 1):
                    if x < h > y:
                        print(f'{x}{y}{ascii_lowercase[i]}{ascii_lowercase[j]}{h}', end=' ')