from math import floor

series_name = input()
seasons_number = int(input())
episodes_number = int(input())
episode_length = float(input())

episode_length += episode_length * 20 / 100
special_episodes = 10 * seasons_number

total = episode_length * episodes_number * seasons_number + special_episodes

print(f'Total time needed to watch the {series_name} series is {floor(total)} minutes.')