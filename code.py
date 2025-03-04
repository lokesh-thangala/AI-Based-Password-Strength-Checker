import re

def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif re.search(r"[A-Z]", password) and re.search(r"[0-9]", password) and re.search(r"[!@#$%^&*]", password):
        return "Strong"
    else:
        return "Moderate"

password = input("Enter a password: ")
print("Strength:", check_password_strength(password))
