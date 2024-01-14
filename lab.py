#create a prgram that will add two-digit numbers

two_digit_number = input("Enter a two-digit number: ")

# Check if the input is a valid two-digit number
if len(two_digit_number) != 2:
    print("Please enter a valid two-digit number.")
else:
    # Extract the first and second digits from the string and convert them to integers
    first_digit = int(two_digit_number[0])
    second_digit = int(two_digit_number[1])

    # Perform addition of the two digits
    result = first_digit + second_digit

    # Print the result
    print(result)
    
#PEMDASL RULES 
# P - Parentheses
# E - Exponents (or Orders, like square roots and cube roots)
# M - Multiplication
# D - Division
# A - Addition
# S - Subtraction
# L - Left to Right
