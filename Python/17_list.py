# List in Python

# (A list is a collection which is ordered and changeable.)

# Creating a list
my_list = [1, 2, 3, "john", True]
print("Original list:", my_list)

# Accessing list items
print("Second item of the list:", my_list[1])

# Changing the value of a list item
my_list[1] = 10
print("Changed list:", my_list)

# Adding an item to the end of the list
my_list.append(4)
print("List after appending 4:", my_list)

# Removing an item from the list
my_list.remove(10)
print("List after removing 10:", my_list)

# Looping through a list
for item in my_list:
    print("Looping item:", item)
