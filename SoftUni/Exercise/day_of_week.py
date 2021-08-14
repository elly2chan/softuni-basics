days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
n = int(input())
index = n

for day in days:
    if index in range(1, len(days) + 1):
        day_is = days[index - 1]
    else:
        day_is = "Error"

print(day_is)