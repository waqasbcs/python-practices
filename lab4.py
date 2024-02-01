print("welcome to the corvit system!! ")
age = int(input("Enter your age: "))
if age >= 18:
    print("you can select ")
else:
    print("you can not select because you age is not greater than 18!!")
    
#write a program that check the number is even or old 
number = int(input("which number do you want to check? "))
if number % 2 == 0:
    print("this is even number.")
else:
    print("this is odd number.")