player_name = input()
best_player = ""
best_score = 0
while player_name != "Stop":
    player_score = 0
    for ch in player_name:
        guess = int(input())
        if guess == ord(ch):
            player_score += 10
        else:
            player_score += 2

    if player_score >= best_score:
        best_player = player_name
        best_score = player_score
    player_name = input()

print(f'The winner is {best_player} with {best_score} points!')