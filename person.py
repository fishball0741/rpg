class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        print(self)
        print(f'Hello, {self.name}!')