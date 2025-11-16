import random
import string

# Passwort generierung mit custom optionen

print("Welcome to the Password Generator!")
print()

# passwort länge
while True:
    try:
        length = int(input("How long should the password be? (minimum 4): "))
        if length < 4:
            print("Password is too short! Please enter at least 4.")
        else:
            break
    except:
        print("Please enter a valid number!")

#  Zeichen Optionen
print()
print("Which character types should be included?")
use_lowercase = input("Lowercase letters (a-z)? (y/n): ").lower()
use_uppercase = input("Uppercase letters (A-Z)? (y/n): ").lower()
use_numbers = input("Numbers (0-9)? (y/n): ").lower()
use_special = input("Special characters (!@#$...)? (y/n): ").lower()

# Build character pool
characters = ""

if use_lowercase == "y":
    characters += string.ascii_lowercase
if use_uppercase == "y":
    characters += string.ascii_uppercase
if use_numbers == "y":
    characters += string.digits
if use_special == "y":
    characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

if characters == "":
    print()
    print("You need to select at least one option!")
    print("Using all character types...")
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Passwort generieren
password = ""
for i in range(length):
    password += random.choice(characters)

#  Passwort anzeigen/result anzeigen
print()
print("="*50)
print("Your generated password:")
print(password)
print("="*50)
print()

# Passwort Stärke checken
strength = 0
if len(password) >= 8:
    strength += 1
if len(password) >= 12:
    strength += 1
if any(c.islower() for c in password):
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1
if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
    strength += 1

if strength <= 2:
    print("Password strength: Weak")
elif strength <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")

print()
