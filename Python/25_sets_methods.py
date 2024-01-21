# set methods in Python

# Initialize a set
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)


# Add an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)


# Remove an element from the set
# my_set.remove(44)     # throws error if the element is not found
# print("Set after removing an element:", my_set)


# Discard an element from the set
my_set.discard(10)  # No error if the element is not found
print("Set after discarding an element:", my_set)


# Pop an element from the set
print("Set before popping an element:", my_set)
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after popping an element:", my_set)


# Clear all elements from the set
my_set.clear()
print("Set after clearing:", my_set)


# Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of two sets:", union_set)


# Intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of two sets:", intersection_set)


# Difference of two sets
difference_set = set1.difference(set2)
print("Difference of two sets:", difference_set)


# Symmetric difference of two sets (elements in either set, but not in both)
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric difference of two sets:", sym_diff_set)
