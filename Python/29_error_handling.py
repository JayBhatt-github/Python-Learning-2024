# error handling in python

# example-1: Multiplication table with error handling for non-integer inputs
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  # Loop to print multiplication table
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  # Exception block to handle non-integer inputs
  print("Invalid  Input!")

# Some important lines of code
print("Some imp lines of code")
print("End of program")

# example-2: Accessing list elements with error handling for non-integer and out of range inputs
try:
    num = int(input("Enter an integer: "))
    b = [6, 3]
    # Attempt to access list element
    print(b[num])
except ValueError:
    # Exception block to handle non-integer inputs
    print("Number entered is not an integer.")
    
except IndexError:
  # Exception block to handle out of range inputs
  print("Index Error")