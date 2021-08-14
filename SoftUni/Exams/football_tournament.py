football_team = input()
games_current_season = int(input())
counter = games_current_season
wins = 0
losses = 0
draws = 0
score = 0

while counter > 0:
    result = input()
    if result == "W":
        wins += 1
        score += 3
    elif result == "L":
        losses += 1
    elif result == "D":
        draws += 1
        score += 1
    counter -= 1

if games_current_season <= 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    print(f'{football_team} has won {score} points during this season.')
    print("Total stats:")
    print(f'## W: {wins}')
    print(f'## D: {draws}')
    print(f'## L: {losses}')
    print(f'Win rate: {(wins / games_current_season * 100):.2f}%')