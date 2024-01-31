# Constructor in Python

# Class definition
class Person:
    # Constructor
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

    # Method to describe the person
    def desc(self):
        print(f"Name:{self.name}\nOccupation:{self.occupation}\nAge:{self.age}\n")

# Creating instances of the Person class
a = Person("Brayden", "Administrator", "31")
b = Person("Chris", "Product Designer", "26")
c = Person("Anderson", "Accountant", "34")

# Describing the instances
a.desc()
b.desc()
c.desc()
