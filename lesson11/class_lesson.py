class Person:

    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age
    
    def say_hello():
        print("Hello, everyone.")

bob = Person(name="bob", nationality="Jamaica", age=67)
print(bob.age, bob.nationality, bob.name)

eric = Person(name="eric", nationality="British", age=75)
print(eric.age, eric.nationality, eric.name)