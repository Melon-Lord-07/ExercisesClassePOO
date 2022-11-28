"""
Sandra Nitchi, 2022
exercise 1
"""

class StringFoo:
    def __init__(self, message):
        self.message = message

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(f"{self.message.upper()}")

str_foo = StringFoo("mayonase".upper())
str_foo.set_string("ur mom")
str_foo.print_string()