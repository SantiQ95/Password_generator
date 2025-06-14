import random
import string

## Random Password Generator
# This class generates a random password based on specified criteria.
class PasswordGenerator:

    # Parameters:
    def __init__(self, max_length=25, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special_chars=True, length= 12, min_length=8):
        self.max_length = max_length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special_chars = use_special_chars
        self.use_lowercase = use_lowercase
        self.length = length
        self.min_length = min_length

    # Generate:
    def generate(self):
        # Build the character set based on selected options
        characters = ""
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_numbers:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation
        if not characters:
            raise ValueError("At least one character type must be selected.")

        # Validate length
        if self.length < self.min_length:
            raise ValueError(f"Password length must be at least {self.min_length}.")
        if self.length > self.max_length:
            raise ValueError(f"Password length must not exceed {self.max_length}.")

        # Generate the password
        return ''.join(random.choice(characters) for _ in range(self.length))
