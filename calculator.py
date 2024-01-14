first_number = input("Enter your first number: ")
operator = input("Enter your operator (+, -, *, %, /, **): ")
second_number = input("Enter your second number: ")

# Convert input strings to integers
first_name = int(first_number)
second_name = int(second_number)

if operator == "+":
    result = first_name + second_name
    print("Result:", result)

elif operator == "-":
    result = first_name - second_name
    print("Result:", result)

elif operator == "*":
    result = first_name * second_name
    print("Result:", result)

elif operator == "%":
    result = first_name % second_name
    print("Result:", result)

elif operator == "/":
    # Checking if the second number is zero to avoid division by zero error
    if second_name == 0:
        print("Error: Division by zero is not allowed")
    else:
        result = first_name / second_name
        print("Result:", result)

elif operator == "**":
    result = first_name ** second_name
    print("Result:", result)

else:
    print("Invalid operator")
