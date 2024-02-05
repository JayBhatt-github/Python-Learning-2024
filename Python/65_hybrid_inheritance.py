# Hybrid Inheritance in Python

# Python program to demonstrate hybrid inheritance
class Office:

    def func1(self):
        print ('This function is in Office.')

class Emp1(Office):

    def func2(self):
        print ('This function is in Employee 1.')

class Emp2:

    def func3(self):
        print ('This function is in Employee 2.')

class Emp3(Emp1, Emp2):

    def func4(self):
        print ('This function is in Employee 3.')

# Driver's code

object = Emp3()
object.func1()
object.func2()
object.func3()
object.func4()


# Explanation:
# In the above example, class B is inheriting the property of class A, and class D inherits the property of class B and class C.