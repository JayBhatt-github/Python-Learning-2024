# Access Modifiers in Python
# Public, Private, Protected and Mangling in Python

class MyClass:
    def __init__(self):
        self.public = "I'm a public attribute"
        self._protected = "I'm a protected attribute"
        self.__private = "I'm a private attribute"

    def show(self):
        print(self.public)
        print(self._protected)
        print(self.__private)

# Creating an object of 'MyClass'
obj = MyClass()

# Accessing public attributes
print(obj.public)

# Accessing protected attributes
print(obj._protected)

# Accessing private attributes directly will raise an error
# print(obj.__private)

# Accessing private attributes using mangling
print(obj._MyClass__private)
