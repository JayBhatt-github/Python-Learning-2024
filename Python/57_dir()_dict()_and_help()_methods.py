# Understanding the concepts of dir(), dict() and help() methods

# dir() method
# The dir() method is used to find out all the attributes and methods of a class or module.
# It returns a sorted list of strings containing the names defined by a module.

class Employee:
  company = "Apple"
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

print(dir(Employee))

# dict() method
# The dict() method is used to create a dictionary.
# It returns a dictionary from a sequence of key-value pairs.

# emp_dict = dict(name="Harry", salary=50000)
# print(emp_dict)

p = Employee("John", 30)
print(p.__dict__)

# help() method
# The help() method is used to get the documentation of modules, classes, functions, keywords, etc.
# It returns the help related to the object passed.

help(Employee)
