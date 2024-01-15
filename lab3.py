# Get the current age as input
current_age = int(input("Please enter your current age: "))

# Get the last age as input
last_age = int(input("Please enter your last age: "))

# Calculate the remaining time
remaining_years = last_age - current_age

# Calculate months, weeks, and days
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

# Display the result
message = (f"Remaining time in terms of:\nMonths: {remaining_months} months\nWeeks: {remaining_weeks} weeks\nDays: {remaining_days} days")
print(message)