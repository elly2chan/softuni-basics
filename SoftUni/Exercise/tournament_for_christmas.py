tournament_days = int(input())
counter = 0
wins = 0
losses = 0
profit = 0

while counter < tournament_days:
    daily_wins = 0
    daily_losses = 0
    daily_profit = 0

    sport = input()
    while sport != "Finish":
        result = input()

        if result == "win":
            daily_wins += 1
            daily_profit += 20
        elif result == "lose":
            daily_losses += 1
        sport = input()

        if sport == "Finish":

            if daily_wins > daily_losses:
                wins += 1
                daily_profit += daily_profit * 10 / 100
                profit += daily_profit
            elif daily_wins < daily_losses:
                losses += 1
                profit += daily_profit
    counter += 1

if wins > losses:
    profit += profit * 20 / 100
    print(f"You won the tournament! Total raised money: {profit:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {profit:.2f}")
