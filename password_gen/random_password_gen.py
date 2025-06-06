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
        characters = string.ascii_lowercase
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_numbers:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation
        if self.length:
            if isinstance(self.length, tuple):
                self.length = random.randint(self.length[0], self.length[1])
            elif isinstance(self.length, int):
                if self.length < 8 or self.length > self.max_length:
                    raise ValueError(f"Length must be between 8 and {self.max_length}.")

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password
    