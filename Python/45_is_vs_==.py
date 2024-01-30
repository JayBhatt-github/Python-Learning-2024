# 'is' vs '==' in python

# 'is' is used to test if two variables refer to the same object.
# '==' is used to test if two variables have the same values.

# Example 1
a = [1, 2, 3]
b = a
print(a is b)  # Output: True
print(a == b)  # Output: True

# Example 2
c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)  # Output: False
print(c == d)  # Output: True
