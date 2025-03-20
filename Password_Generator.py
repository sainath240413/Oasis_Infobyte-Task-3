import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generate a random password based on user preferences."""
    character_pool = ""

    if use_letters:
        character_pool += string.ascii_letters  # Includes both uppercase and lowercase letters
    if use_numbers:
        character_pool += string.digits  # Includes numbers 0-9
    if use_symbols:
        character_pool += string.punctuation  # Includes special characters

    if not character_pool:
        print("You must select at least one character type!")
        return None

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

# Get user input
try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        use_letters = input("Include letters? (y/n): ").strip().lower() == "y"
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            print(f"\nGenerated Password: {password}")

except ValueError:
    print("Invalid input. Please enter a numeric value for length.")
