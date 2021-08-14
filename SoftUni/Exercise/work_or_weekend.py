day = input()

if day == "Saturday" or day == "Sunday":
    print("Weekend")
elif day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print("Working day")
else:
    print("Error")