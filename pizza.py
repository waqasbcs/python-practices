print("welcome to pizza deliveries! ")
size = input("what is the size of pizza you want? S, M, or L ")
add_pepperoni = input("do you want pepperoni? Y or N ")
extra_cheese = input("do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")
