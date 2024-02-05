
# Define a class A
class A:
    def method(self):
        print("This is from class A")

# Define a class B
class B:
    def method(self):
        print("This is from class B")

# Define a class C that inherits from both A and B
class C(A, B):
    pass

# Create an object of class C
obj = C()

# Call the method of class A
obj.method()
