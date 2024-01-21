# tuple operations in python


my_tuple = (1, 2, 3, 4, 5)
print("Original my_tuple", my_tuple)

# Slicing tuples
print("Elements from index 1 to 4:", my_tuple[1:5])

# Tuple concatenation
another_tuple = (6, 7, 8)
print("Original another_tuple", another_tuple)

concatenated_tuple = my_tuple + another_tuple
print("Concatenated Tuple:", concatenated_tuple)

# Tuple repetition
repeated_tuple = my_tuple * 3
print("Repeated Tuple:", repeated_tuple)

# Tuple length
print("Length of Tuple:", len(my_tuple))

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked:", a, b, c, d, e)

# Checking if an item exists in a tuple
if 3 in my_tuple:
    print("Yes, 3 is in the tuple")

# Iterating through a tuple
for item in my_tuple:
    print(item)

# Tuple methods
# count() - Returns the number of times a specified value occurs in a tuple
count_of_item = my_tuple.count(3)
print("Count of '3':", count_of_item)

# index() - Searches the tuple for a specified value and returns the position of where it was found
index_of_item = my_tuple.index(3)
print("Index of '3':", index_of_item)
