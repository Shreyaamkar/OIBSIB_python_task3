import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters   # a-z A-Z
    if use_numbers:
        characters += string.digits          # 0-9
    if use_symbols:
        characters += string.punctuation     # symbols

    if not characters:
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    use_letters = input("Include letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password is None:
        print("You must select at least one character type.")
    else:
        print("\n✅ Generated Password:")
        print(password)


if __name__ == "__main__":
    main()
