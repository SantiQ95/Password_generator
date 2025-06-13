from password_gen.random_password_gen import PasswordGenerator

# Create a default instance to access default parameter values
DEFAULTS = PasswordGenerator()
DEFAULT_LENGTH = DEFAULTS.length
MIN_LENGTH = DEFAULTS.min_length
MAX_LENGTH = DEFAULTS.max_length

def ask_bool(prompt, default=True):
    """
    Ask the user a yes/no question.
    If the user presses Enter, the default value is used.
    """
    resp = input(f"{prompt} (y/n, Enter for default {'y' if default else 'n'}): ").strip().lower()
    if resp == "":
        return default
    return resp == "y"

def ask_length(prompt, default=DEFAULT_LENGTH, min_length=MIN_LENGTH, max_length=MAX_LENGTH):
    """
    Ask the user for a password length.
    If the user presses Enter, the default value is used.
    Ensures the length is an integer within the allowed range.
    """
    resp = input(f"{prompt} (must be an integer, min {min_length}, max {max_length}, Enter for default {default}): ").strip()
    if resp == "":
        return default
    try:
        val = int(resp)
        if val < min_length:
            print(f"Error: Length must be at least {min_length}. Using default ({default}).")
            return default
        if val > max_length:
            print(f"Error: Length must not exceed {max_length}. Using default ({default}).")
            return default
        return val
    except ValueError:
        print("Invalid input: length must be an integer. Using default.")
        return default

if __name__ == "__main__":
    print("=== Password Generator ===")
    # Ask the user for each password option, using class defaults if Enter is pressed
    use_uppercase = ask_bool("Allow uppercase letters?", default=DEFAULTS.use_uppercase)
    use_lowercase = ask_bool("Allow lowercase letters?", default=DEFAULTS.use_lowercase)
    use_numbers = ask_bool("Allow numbers?", default=DEFAULTS.use_numbers)
    use_special_chars = ask_bool("Allow special characters?", default=DEFAULTS.use_special_chars)
    length = ask_length("Password length?", default=DEFAULT_LENGTH, min_length=MIN_LENGTH, max_length=MAX_LENGTH)

    # Create the password generator with the selected options
    gen = PasswordGenerator(
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_numbers=use_numbers,
        use_special_chars=use_special_chars,
        length=length
    )
    # Generate and display the password
    password = gen.generate()
    print(f"\nGenerated password: {password}")