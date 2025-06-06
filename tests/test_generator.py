# test 

from password_gen.random_password_gen import PasswordGenerator

def test_generate_default():
    gen = PasswordGenerator()
    password = gen.generate()
    assert isinstance(password, str)
    assert 8 <= len(password) <= 25

def test_generate_custom_length():
    gen = PasswordGenerator(length=(12, 16))
    password = gen.generate()
    assert 12 <= len(password) <= 16

def test_generate_only_lowercase():
    gen = PasswordGenerator(use_uppercase=False, use_numbers=False, use_special_chars=False)
    password = gen.generate()
    assert password.islower()

if __name__ == "__main__":
    test_generate_default()
    test_generate_custom_length()
    test_generate_only_lowercase()
    print("All tests passed!")