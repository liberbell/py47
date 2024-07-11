class Person:

    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age

bob = Person(name="bob", nationality="Jamaica", age=67)
print(bob.age, bob.nationality, bob.name)