# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to use the add function inside it
def add_and_square(a, b):
    # Call the add function and store the result in a variable
    sum = add(a, b)
    # Return the square of the result
    return sum ** 2

# Call the add_and_square function
result = add_and_square(3, 5)
print("The result is:", result)



# Other example

# Define a function to use the add function as an argument
def operation_on_add(func, x, y):
    # Call the add function and store the result in a variable
    sum = add(x, y)
    # Call the function passed as an argument on the sum
    return func(sum)

# Define a function to double a number
double = lambda x: x * 2

# Call the operation_on_add function
result = operation_on_add(double, 3, 5)
print("The result of operation_on_add is:", result)
