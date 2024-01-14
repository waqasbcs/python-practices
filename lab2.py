#BMI CALCULATOR:

height = input("Enter your height in meters: ")
weight = input("Enter your weight in kg: ")

# Convert height and weight to float
height_float = float(height)
weight_float = float(weight)

# Calculate BMI
BMI = weight_float / (height_float ** 2)

# Round BMI to the nearest whole number
rounded_BMI = round(BMI)

# Print the rounded result
print("Rounded BMI:", rounded_BMI)

# it is used for integer 

# print(type(8 // 2 ))