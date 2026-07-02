import re
import random
import string

# List of common passwords
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty",
    "admin", "welcome", "abc123", "password123"
]

# Function to generate a strong password suggestion
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to analyze password strength
def analyze_password(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        suggestions.append("Use at least 12 characters for better security.")
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("This is a very common password. Avoid using it.")
        score = max(0, score - 2)

    # Repeated Character Check
    if re.search(r"(.)\1{2,}", password):
        suggestions.append("Avoid repeated characters (e.g., aaa, 111).")
        score -= 1

    # Determine Strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions

# Main Program
print("===== PASSWORD STRENGTH ANALYZER =====")

password = input("Enter your password: ")

strength, suggestions = analyze_password(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions to Improve:")
    for s in suggestions:
        print("-", s)

if strength != "Strong":
    print("\nSuggested Strong Password:")
    print(generate_strong_password())

print("\nAnalysis Complete!")