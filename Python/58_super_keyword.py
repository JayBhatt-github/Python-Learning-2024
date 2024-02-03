# Super keyword in Python

class Parent:
    def __init__(self):
        print("Parent class constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class constructor")

# Creating an object of Child class
obj = Child()
