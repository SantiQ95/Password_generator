from setuptools import setup, find_packages

setup(
    name="password_generator",
    version="0.1.0",
    description="A random password generator with customizable options.",
    author="Santiago Quintanilla",
    packages=find_packages(exclude=["password_gen_env", "tests", "Scripts", "__pycache__"]),
    install_requires=[
        # List external dependencies here (if any)
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            # This allows the script to be run from the command line as 'passwordgen'
             "passwordgen=Scripts.main:main",
        ]
    },
    include_package_data=True,
    zip_safe=False,
)