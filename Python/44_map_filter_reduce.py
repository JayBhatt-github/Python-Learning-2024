# Map, Filter, and Reduce in Python

# Import the reduce function from the functools module
from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Map: Use the map function to double each number in the list
doubled = list(map(lambda x: x * 2, numbers))

# Filter: Use the filter function to keep only the even numbers in the list
even = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce: Use the reduce function to calculate the sum of the numbers in the list
sum = reduce(lambda x, y: x + y, numbers)  # it will take x and y from numbers (from number first 2 elements)

#demonstrate above statement execution
# numbers = [1, 2, 3, 4, 5]  here  x + y = 1 + 2
# numbers = [3(1+2), 3, 4, 5]  here  x + y = 3 + 3
# numbers = [6(3+3), 4, 5]  here x + y = 6 + 4
# numbers = [10(6+4), 5]  here x + y = 10 + 5
# numbers = [15(10+5)]  ans = 15


# Print the results
print("Doubled:", doubled)
print("Even numbers:", even)
print("Sum:", sum)
