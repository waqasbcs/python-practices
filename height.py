# Define a list of heights (in centimeters)
heights = [170, 165, 180, 175, 160]

# Initialize variables to store the total sum of heights and the number of people
total_height = 0
num_people = len(heights)

# Iterate over each height in the list using a for loop
for height in heights:
    # Add each height to the total sum
    total_height += height

# Calculate the average height
average_height = total_height / num_people

# Print the average height
print(f"The average height of the group is: {average_height} cm")
