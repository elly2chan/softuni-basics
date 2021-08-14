hour = int(input())
day = input()

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if hour in range(10, 19):
    if day in working_days:
        print("open")
    else:
        print("closed")
else:
    print("closed")
