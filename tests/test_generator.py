import pytest
from password_gen.random_password_gen import PasswordGenerator

DEFAULTS = PasswordGenerator()

def test_generate_default():
    # Test default parameters: should return a string of default length
    gen = PasswordGenerator()
    password = gen.generate()
    assert isinstance(password, str)
    assert gen.min_length <= len(password) <= gen.max_length

def test_generate_custom_length():
    # Test custom length within allowed range
    gen = PasswordGenerator(length=16)
    password = gen.generate()
    assert len(password) == 16

def test_generate_min_length():
    # Test password with minimum allowed length
    gen = PasswordGenerator(length=DEFAULTS.min_length)
    password = gen.generate()
    assert len(password) == DEFAULTS.min_length

def test_generate_max_length():
    # Test password with maximum allowed length
    gen = PasswordGenerator(length=DEFAULTS.max_length)
    password = gen.generate()
    assert len(password) == DEFAULTS.max_length

def test_generate_only_lowercase():
    # Test password with only lowercase letters
    gen = PasswordGenerator(use_uppercase=False, use_numbers=False, use_special_chars=False, use_lowercase=True)
    password = gen.generate()
    assert password.islower()

def test_generate_only_uppercase():
    # Test password with only uppercase letters
    gen = PasswordGenerator(use_lowercase=False, use_numbers=False, use_special_chars=False, use_uppercase=True)
    password = gen.generate()
    assert password.isupper()

def test_generate_only_numbers():
    # Test password with only numbers
    gen = PasswordGenerator(use_uppercase=False, use_lowercase=False, use_special_chars=False, use_numbers=True)
    password = gen.generate()
    assert password.isdigit()

def test_generate_only_special_chars():
    # Test password with only special characters
    gen = PasswordGenerator(use_uppercase=False, use_lowercase=False, use_numbers=False, use_special_chars=True)
    password = gen.generate()
    import string
    assert all(char in string.punctuation for char in password)

def test_length_below_min_raises():
    # Test that ValueError is raised if length is below min_length
    gen = PasswordGenerator(length=DEFAULTS.min_length - 1)
    with pytest.raises(ValueError):
        gen.generate()

def test_length_above_max_raises():
    # Test that ValueError is raised if length is above max_length
    gen = PasswordGenerator(length=DEFAULTS.max_length + 1)
    with pytest.raises(ValueError):
        gen.generate()

def test_no_character_types_selected():
    # Test that ValueError is raised if no character types are selected
    gen = PasswordGenerator(use_uppercase=False, use_lowercase=False, use_numbers=False, use_special_chars=False)
    with pytest.raises(ValueError):
        gen.generate()

if __name__ == "__main__":
    pytest.main()
    print("All tests passed!")