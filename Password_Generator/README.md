# Password Generator

A simple Python password generator that creates secure passwords based on user-selected criteria. Users can generate letter-only, numeric-only, or mixed passwords with a custom length.

The project demonstrates object-oriented programming concepts such as inheritance, abstraction, and polymorphism using Python's `abc` module.

## Features

* Generate alphabetic passwords
* Generate numeric passwords
* Generate mixed passwords (letters and numbers)
* User-defined password length
* Object-oriented design with abstract base classes
* Lightweight and easy to use

## Password Types

| Type    | Description                              |
| ------- | ---------------------------------------- |
| Letter  | Contains uppercase and lowercase letters |
| Numeric | Contains digits only                     |
| Mixed   | Contains both letters and digits         |

## Technologies Used

* Python 3
* abc (Abstract Base Classes)
* string
* random

## Project Structure

```text
password_generator/
│
├── password_generator.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

## Usage

Run the script:

```bash
python password_generator.py
```

Example interaction:

```text
'Letter' Password, 'Numeric' Password Or 'Mixed' Password ? Mixed
Length of Password: 12

Generated Password:
A9kP7mX2Qz4L
```

## How It Works

The application uses an abstract base class called `PasswordGenerator` that defines a common interface:

```python
class PasswordGenerator(ABC):
    @abstractmethod
    def generate_password(self, length):
        pass
```

Three subclasses implement different password-generation strategies:

* `LetterPasswordGenerator`
* `NumericPasswordGenerator`
* `MixedPasswordGenerator`

Depending on the user's selection, the appropriate generator is instantiated and used to create a password.

## Example Outputs

### Letter Password

```text
sGhTrQaLpW
```

### Numeric Password

```text
4839501742
```

### Mixed Password

```text
aB7xP3qK9L
```

## Learning Objectives

This project demonstrates:

* Abstract classes
* Inheritance
* Method overriding
* User input handling
* Random data generation
* Object-oriented programming principles

## License

This project is open source and available under the MIT License.
