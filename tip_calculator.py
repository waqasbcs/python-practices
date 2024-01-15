print("Welcome to my tip calculator!!")
bill = float(input("What is the total bill? PKR "))
tip_percentage = int(input("How much tip would you like to give? 1, 2, 3, 4, 5, or 10? "))
people = int(input("How many people to split the bill with? "))

# Calculate tip amount and total bill
tip_as_percent = tip_percentage / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# Calculate amount per person
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# Display results
print(f"\nTotal Bill: PKR {bill:.2f}")
print(f"Tip Percentage: {tip_percentage}%")
print(f"Tip Amount: PKR {total_tip_amount:.2f}")
print(f"Total Amount (including tip): PKR {total_bill:.2f}")
print(f"Each person should pay: PKR {final_amount:.2f}")
