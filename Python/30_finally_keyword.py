# finally in python
"""
The finally keyword in Python is used in exception handling to specify a block of code to be executed, 
no matter if an error occurs or not. The finally block always executes after normal termination of try block 
or after try block terminates due to some exception.
"""

# Example of finally keyword in Python
def division(a, b):
    try:
        result = a / b
        print(f"The result is {result}")
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except TypeError:
        print("Please provide numbers for division.")
    finally:
        # This block will always be executed, regardless of exception occurrence
        print("Executing finally block.")

# Call the function with proper arguments
division(10, 2)
division(5, 0)
division('10', '2')

# Important Notes:
# 1. The finally block is optional in the try-except statement.
# 2. It is used to define clean-up actions that must be executed under all circumstances.
# 3. A finally block will run whether or not an exception is caught in the try block.
# 4. If an exception is thrown, but not caught in the except block, the finally block will still execute before the exception is propagated.
# 5. It's a good place to release external resources such as files or network connections.

