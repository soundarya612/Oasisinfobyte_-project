import random
import string
def generate_password(length=12):
    characters=string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choice(characters)for i in range(length))
    
    return password

try:
    length= int(input("enter the desired password length(minimum 8 characters):"))
    if length < 8:
        print("password length should be at least 8 characters.setting default length to 12")
        length=12
except ValueError:
    print("invalid input.setting default length to 12")
    length=12

generated_password = generate_password(length)
print(f"your generated password is: {generated_password}")
