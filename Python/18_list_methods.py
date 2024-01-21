# list methods in python

my_list = [1,2,3,4,5,6,7,8,9,10,11]
print("Original List:", my_list)


# append() - Adds an element at the end of the list
my_list.append(11)
print("List after append:", my_list)

# insert() - Adds an element at a specified position
my_list.insert(2, 0)        # 0 to be inserted in 2nd index position
print("List after insert:", my_list)

# sort() - Sorts the list in ascending order
# Note: sort() only works when the list elements are of the same type
numeric_list = [3, 1, 4, 5, 9, 9, 2]
print("Original Numeric list:", numeric_list)

numeric_list.sort()
print("Numeric list after sort:", numeric_list)

# extend() - Adds elements of a list to the end of the current list
another_list = ['extend', 'with', 'list']
my_list.extend(another_list)
print("List after extend:", my_list)

# reverse() - Reverses the order of the list
my_list.reverse()
print("List after reverse:", my_list)

# index() - Returns the index of the first element with the specified value
index_of_item = my_list.index(11)
print("Index of '11':", index_of_item)

# count() - Returns the number of elements with the specified value
count_of_item = my_list.count(11)
print("Count of '11':", count_of_item)

# copy() - Returns a copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)
