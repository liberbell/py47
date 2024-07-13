class Person:

    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age
    
    def say_hello(self, name):
        print(f"Hello {name}, everyone. I am {self.name}")

bob = Person(name="bob", nationality="Jamaica", age=67)
print(bob.age, bob.nationality, bob.name)
bob.say_hello("hepp")

eric = Person(name="eric", nationality="British", age=75)
print(eric.age, eric.nationality, eric.name)
eric.say_hello("hepp")