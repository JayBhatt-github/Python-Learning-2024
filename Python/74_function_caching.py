# Function Caching in Python

# Function caching is a technique used to store the results of expensive function calls
# and return the cached result when the same inputs occur again.
# This is particularly useful when the function is called with the same inputs multiple times.
# Python provides a built-in function called 'functools.lru_cache' to implement function caching.

import functools
import time

# Define a function that takes some time to compute
@functools.lru_cache(maxsize=32)
def expensive_function(n):
    time.sleep(2)
    return (f"The square of {n} is: {n * n}")

# Call the function with the same input multiple times
print(expensive_function(2))
print("Execution completed for 2")
print(expensive_function(5))
print("Execution completed for 5")
print(expensive_function(9))
print("Execution completed for 9")


# This code will run without any delay because it has already been executed and since we used functools.lru_cache, it has the result of the executed calculation
print(expensive_function(2))
print("Execution completed for 2")
print(expensive_function(5))
print("Execution completed for 5")
print(expensive_function(9))
print("Execution completed for 9")



# The function is only computed once for each unique input
# and the result is cached for subsequent calls with the same input.
# This can significantly improve the performance of the program.
