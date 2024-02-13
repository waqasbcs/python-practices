import random
import string

def generate_password(length=12):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation


    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage
password = generate_password()
print("Generated Password:", password)
