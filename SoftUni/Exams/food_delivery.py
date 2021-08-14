chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

total = chicken_menu_count * 10.35 + fish_menu_count * 12.40 + vegetarian_menu_count * 8.15
desert = total * 20 / 100

print(f'Total: {(total + desert + 2.50):.2f}')