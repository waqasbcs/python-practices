import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r','s',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C','D','E','F', 'G', 
           'H', 'I', 'J', 'K','L', 'M', 'N', 'O','P','Q',
           'R','S','T','U','V','W','X','Y','Z']
numbers  = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','<','>','&','@','*','?','/','%','|',':','=','+',';','=']

print("Welcome to password generator!!! ")

nu_letters = int(input(f"how many letters do you like to generate your password? \n "))
nu_numbers = int(input(f"how many numbers do you like to generate your password? \n "))
nu_symbols = int(input(f"how many symbols do you like to generate your password? \n "))

#easyway to generate password

password = ""

for char in range(1 ,nu_letters + 1):
    password += random.choice(letters)
    
for char in range(1 ,nu_numbers +1):
    password += random.choice(numbers)
    
for char in range(1 ,nu_symbols +1):
    password += random.choice(symbols)
    
print(password)







