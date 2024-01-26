# Custom Errors in Python
"""
In Python, we can also create our own exceptions and errors using the 'raise' keyword. 
We can add a condition in the program where we need to raise an error if the condition is met.
"""


a = int(input("Enter any value between 5 and 9:"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 