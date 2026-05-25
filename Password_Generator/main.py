from abc import ABC, abstractmethod
import string
import random

Ptypes = ["Letter","Numeric","Mixed"]

class PasswordGenerator(ABC):
    @abstractmethod
    def generate_password(self, length):
        pass

class NumericPasswordGenerator(PasswordGenerator):
    letters = string.digits
    def generate_password(self, length):
        for i in range(length):
            result = ''.join(str(random.choice(self.letters)) for _ in range(length))
        return result

class LetterPasswordGenerator(PasswordGenerator):
    letters = string.ascii_letters
    def generate_password(self, length):
        for i in range(length):
            result = ''.join(str(random.choice(self.letters)) for _ in range(length))
        return result


class MixedPasswordGenerator(PasswordGenerator):
    letters = string.ascii_letters + string.digits
    def generate_password(self, length):
        for i in range(length):
            result = ''.join(str(random.choice(self.letters)) for _ in range(length))
        return result


Ptype = None
while Ptype not in Ptypes:
    Ptype = input("'Letter' Password, 'Numeric' Password Or 'Mixed' Password ? ")

len = input("Length of Password: ")
while len == string.digits:
    len = input("Length of Password: ")

if Ptype == "Letter":
    generator = LetterPasswordGenerator()
    password = generator.generate_password(int(len))
    print(password)
elif Ptype == "Numeric":
    generator = NumericPasswordGenerator()
    password = generator.generate_password(int(len))
    print(password)
else:
    generator = MixedPasswordGenerator()
    password = generator.generate_password(int(len))
    print(password)
