import random
import string

def generate_password(length, complexity):
    char_sets = {
        '1': string.ascii_lowercase,
        '2': string.ascii_lowercase + string.ascii_uppercase,
        '3': string.ascii_letters + string.digits,
        '4': string.ascii_letters + string.digits + string.punctuation
    }

    # Get character set based on complexity
    chars = char_sets[complexity]
    
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# User input
length = int(input("Enter the length of the password: "))
print("Select complexity level:")
print("1: Lowercase")
print("2: Lowercase and Uppercase")
print("3: Alphanumeric")
print("4: Alphanumeric with Symbols")
complexity = input("Enter complexity level (1-4): ")

# Generate and display the password
password = generate_password(length, complexity)
print(f"Generated Password: {password}")

# Password strength rating
def password_strength(password):
    strength = len(set(password))
    if strength < 10:
        return "Weak"
    elif strength < 20:
        return "Moderate"
    else:
        return "Strong"

print(f"Password Strength: {password_strength(password)}")
