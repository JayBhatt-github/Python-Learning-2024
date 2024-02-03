# Dunder (Double Underscore) or Magic Methods in Python

class Employee:

  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

  def __call__(self):       #this method will be called automatically when you write "e()"
    print("Hey I am good")


e = Employee("John")
print(str(e))
print(repr(e))
e()     # it will call (__call__) method automatically