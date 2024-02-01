# Inheritance in Python.

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("John Doe", 400)
e1.showDetails()
e2 = Programmer("Peter", 4100)
e2.showDetails()
e2.showLanguage()
