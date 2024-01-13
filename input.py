# sourcery skip: avoid-builtin-shadow, use-fstring-for-concatenation
first_name = input("Please enter your first_name?\n ")
print(f"first_name: {first_name}")

last_name = input("Please enter your last_name?\n ")
print("last_name:"  +  last_name)


username = input("enter your username?\n" )
print(username)


print("passowrd: " + input("Enter your password!!!\n " ))


email = input("Please enter your email address? ")
print(len(email))
#len is user for counter

address = input("Please enter your address? ")
length = len(address)
print(length)


first = input("Enter your first number:" )
second = input("Enter your second number:" )

sum = int(first) + int(second)
print("the sum is : " + str(sum))

name = "waqas khan"
print(name.upper())


name = "waqas khan"
print(name.lower())

name = "waqas khan"
#index start from 0 
#if the string is not find it will return -1
print(name.find("k"))

name = "waqas khan"
print(name.replace("waqas khan", "maryam waqas"))




