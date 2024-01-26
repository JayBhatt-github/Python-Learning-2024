# working of import in python

# The import function in Python is used to import modules into your current script.
# Here's an example of how to use the import function:

# Import the math module
import math

# Now we can use functions from the math module, for example:
print(math.sqrt(16))  # This will print 4.0, as the square root of 16 is 4.

# If you only need a specific function from a module, you can import just that function:
from math import sqrt

# Now we can use the sqrt function directly, without the need to reference the math module:
print(sqrt(25))  # This will print 5.0, as the square root of 25 is 5.

# If you want to import a module with a different name, you can use the 'as' keyword:
import math as m
print(m.sqrt(36))  # This will print 6.0, as the square root of 36 is 6.

# You can also import all functions from a module using the '*' wildcard, although this is not recommended as it can lead to namespace collisions:
from math import *
print(sqrt(49))  # This will print 7.0, as the square root of 49 is 7.

# You can also import from user defined files. For example, if we have a file named 'my_module.py' in the same directory as this script, 
# and it contains a function 'my_function', we can import and use it as follows:

# from my_module import my_function
# my_function()
