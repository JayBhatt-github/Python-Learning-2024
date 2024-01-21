# doc string in python

# (python docstrings are the string literals that appear right after the definition of a function, method, class, or module.)

def greet(name):
    """             
    This function greets to the person passed in as a parameter
    """
    # we can also use (''')
    print("Hello, " + name + ". Good morning!")

greet('John')
print(greet.__doc__)    # this will print the doc string that is written after the function/ class/ module / method definition
