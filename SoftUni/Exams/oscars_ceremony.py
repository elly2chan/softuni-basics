rent = int(input())

statues = rent - (rent * 30 / 100)
catering = statues - (statues * 15 / 100)
sound = catering / 2

expenses = rent + statues + catering + sound

print(f'{expenses:.2f}')