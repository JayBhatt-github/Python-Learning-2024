# The walrus operator (:=) was introduced in Python 3.8
# It is used to assign values to variables as part of an expression
# This can be useful when you want to avoid repeating an expression
# or when you want to improve the readability of your code


# Example 1: Assigning a value to a variable and using it in an expression
x = 10
if (y := x + 1) > 10:
    print(f"y is {y}, which is greater than 10")

# Example 2: Example of how you can use the Walrus Operator in a while loop:
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())
    