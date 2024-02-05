row1 = ["💖","💖","💖"]
row2 = ["💖","💖","💖"]
row3 = ["💖","💖","💖"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("where you want to put the trasure? ")

horizontal = int(position[0]) 
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "w"
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "W"

print(f"{row1}\n{row2}\n{row3}")






