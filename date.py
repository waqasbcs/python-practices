import calendar
import datetime

yy = 2024
mm = 1

# Get the current date
today = datetime.date.today()

# Print the calendar header
print(" Mo Tu We Th Fr Sa Su")
print("+---------------------+")

# Print the calendar, marking the current date
cal = calendar.TextCalendar()
for week in cal.monthdayscalendar(yy, mm):
    print("|", end=" ")
    for day in week:
        if day == 0:
            # Print a space for days outside the month
            print("   ", end=" ")
        elif day == today.day:
            # Highlight the current date without color
            print(f"\033[1;31m{day:2d}\033[0m", end=" ")
        else:
            print(f"{day:2d}", end=" ")
    print("|")

print("+---------------------+")
