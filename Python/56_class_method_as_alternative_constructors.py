# Tusing class methods as alternative constructors.

class Employee:
  company = "Apple"
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def show(self):
    print(f"The name is {self.name}, company is {self.company} and salary is {self.salary}")

  @classmethod
  def from_string(cls, emp_string):
    # name, salary = emp_string.split("-")
    name = emp_string.split("-")[0]
    salary = emp_string.split("-")[1]
    return cls(name, salary)

# using normal constructor 
e1 = Employee("deven", 50000)
e1.show()

# using alternative constructors by using class methods
e2 = Employee.from_string("Harry-60000")
e2.show()

# The above code demonstrates the use of a class method as an alternative constructor in Python.
# We have a class Employee with a regular __init__ constructor.
# We also have a class method 'from_string' which takes a string in the format "name-salary" and returns a new instance of Employee.
# We create an instance 'e1' of the Employee class using the regular constructor and display its details.
# We then create an instance 'e2' of the Employee class using the class method 'from_string' and display its details.
