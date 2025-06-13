# Password Generator

A customizable random password generator written in Python.

## Features

- Generate secure passwords with customizable options.
- Choose to include/exclude uppercase, lowercase, numbers, and special characters.
- Set the desired password length (with configurable minimum and maximum).
- Easy-to-use command-line interface.

## Installation

1. **Clone this repository:**
   ```sh
   git clone https://github.com/SantiQ95/password_generator.git
   cd password_generator
   ```

2. **Create and activate a virtual environment (recommended):**
   ```sh
   python -m venv password_gen_env
   password_gen_env\Scripts\activate
   ```

3. **Install the package:**
   ```sh
   pip install .
   ```

4. *(Optional, for development)*  
   Install test dependencies:
   ```sh
   pip install pytest
   ```

## Usage

### As a Python module

You can use the `PasswordGenerator` class in your own scripts:

```python
from password_gen.random_password_gen import PasswordGenerator

gen = PasswordGenerator(length=16, use_uppercase=True, use_numbers=True, use_special_chars=True)
password = gen.generate()
print(password)
```

### From the command line

Run the interactive script:

```sh
python Scripts/main.py
```

You will be prompted to customize your password options or use the defaults.

## Running Tests

To run the test suite, make sure you are in the project root and run:

```sh
pytest
```

Or, if you want to run a specific test file:

```sh
pytest tests/test_generator.py
```

## Project Structure

```
password_gen/         # Main package
  __init__.py
  random_password_gen.py
Scripts/              # CLI script
  main.py
tests/                # Unit tests
  test_generator.py
setup.py              # Package configuration
requirements.txt      # (Optional) List of dependencies
.env                  # (Optional) PYTHONPATH for VS Code
```

## License

MIT License

---

**Author:** Santiago Quintanilla 
**Repository:** [\[GitHub link](https://github.com/SantiQ95/Password_generator)