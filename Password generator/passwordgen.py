import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    return ''.join(random.choice(all_characters) for _ in range(length))

# Define the desired length for the password
password_length = 50

# Generate and display the password
print("Your generate password is : ", generate_password(password_length))
