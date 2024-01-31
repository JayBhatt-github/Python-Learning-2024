# Decorators in Python

# A decorator is a function that takes another function as an argument and adds some kind of functionality to it.
# The following example demonstrates a simple decorator that converts the result of a function to uppercase.

# Decorator function
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

# Function to be decorated
def greet():
    return 'hello!'

# Decorating the function
greet = uppercase_decorator(greet)

# Calling the decorated function
print(greet())

# The above code can be simplified using the @ symbol, which is a shorthand for the decorator syntax.
# The following example achieves the same result as the previous one, but with a simpler syntax.

# Decorator function
def lowercase_decorator(func):
    def wrapper2():
        result = func()
        return result.lower()
    return wrapper2

# Decorating the function
@lowercase_decorator
def greet2():
    return 'HELLO!'

# Calling the decorated function
print(greet2())
