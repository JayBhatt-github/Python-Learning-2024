
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



# Other Example
# Python program to demonstrate multiple inheritances

# Base class1
class A:

    aname = ''

    def aclass(self):
        print (self.aname)

# Base class2

class B:

    bname = ''

    def bclass(self):
        print (self.bname)

# Child class

class C(A, B):

    def cname(self):
        print ('B :', self.bname)
        print ('A :', self.aname)

s1 = C()
s1.bname = 'John'
s1.aname = 'Doe'
s1.cname()