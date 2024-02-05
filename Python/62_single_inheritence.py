# Single Inheritance in Python
class Parent:
    def __init__(self):
        print("This is the parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is the child class")

# Creating an object of the child class
child_obj = Child()
