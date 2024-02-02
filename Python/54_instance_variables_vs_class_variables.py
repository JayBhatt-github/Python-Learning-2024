# instance variable vs class variable in python.

class Employee:
  # Class variables are shared among all instances of a class.
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name  # This is an instance variable. It is unique to each instance.
    self.raise_amount = 0.02  # This is also an instance variable.
    Employee.noOfEmployees +=1  # We use the class name to access the class variable.
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Creating an instance of the Employee class.
emp1 = Employee("Harry")
emp1.raise_amount = 0.3  # We can also change the value of an instance variable for a particular instance.
emp1.companyName = "Apple India"  # Similarly, we can change the value of a class variable for a particular instance.
emp1.showDetails()
Employee.companyName = "Google"  # We can also change the value of a class variable using the class name.
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"  # Changes to class variables made by one instance do not affect other instances.
emp2.showDetails()