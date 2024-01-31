# This is a simple example of using getter and setter in Python.
# The class 'MyClass' has a private variable '_value' which can be accessed and modified using getter and setter methods.

class MyClass:
  # The constructor method initializes the private variable '_value' with the given 'value'.
  def __init__(self, value):
      self._value = value
    
  # This method prints the current value of '_value'.
  def show(self):
    print(f"Value is {self._value}")
    
  # The 'ten_value' method is decorated with '@property', making it a getter for the private variable '_value'.
  # It returns the value of '_value' multiplied by 10.
  @property
  def ten_value(self):
      return 10* self._value
    
  # The 'ten_value' method is decorated with '@ten_value.setter', making it a setter for the private variable '_value'.
  # It sets the value of '_value' to the new value divided by 10.
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10

# Creating an object of 'MyClass' with an initial value of 10.
obj = MyClass(10)

# Setting the 'ten_value' of the object to 67.
obj.ten_value = 67

# Printing the current 'ten_value' of the object.
print(obj.ten_value)

# Printing the current value of the object.
obj.show()