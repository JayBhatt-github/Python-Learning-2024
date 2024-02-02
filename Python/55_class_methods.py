# This is an example of class method in Python.

class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):     # here cls --> self class
    cls.company = newCompany


e1 = Employee()
e1.name = "deven"
e1.show()
e1.changeCompany("Tesla")
e1.show()

print(Employee.company)

# The above code demonstrates the use of a class method in Python.
# We have a class Employee with a class variable 'company' set to "Apple".
# The class method 'changeCompany' is used to change the value of 'company' for all instances of the class.
# We create an instance 'e1' of the Employee class, set its name to "Harry", and display its details.
# We then use the class method 'changeCompany' to change the 'company' value to "Tesla" for all instances.
# We display the details of 'e1' again to see the updated 'company' value.
# Finally, we print the 'company' value directly from the Employee class.
