# dictionary methods in python

# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'location': 'Wonderland'}
print("Dictionary:", my_dict)


# Accessing dictionary values by keys
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])


# Adding a new key-value pair to the dictionary
my_dict['email'] = 'alice@example.com'
print("Dictionary after adding email:", my_dict)


# Updating a value in the dictionary
my_dict.update({'email': 'new_email@example.com'})
print("Dictionary after update method:", my_dict)


# Updating a value in the dictionary
my_dict['age'] = 26
print("Dictionary after updating age:", my_dict)


# Removing a key-value pair using pop
removed_value = my_dict.pop('location')
print("Removed value:", removed_value)
print("Dictionary after removing location:", my_dict)


# Using 'del' to remove a key-value pair from the dictionary
del my_dict['email']
print("Dictionary after deleting email:", my_dict)


# Using get method to avoid KeyError
print("Email:", my_dict.get('email', 'Not found'))
print("Phone:", my_dict.get('phone', 'Not Found'))  # Returns 'Not found' as 'phone' is not a key in the dictionary
print(my_dict)
my_dict['phone'] = "91823"
print(my_dict)


# Iterating over a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")


# Checking if a key exists in a dictionary
if 'name' in my_dict:
    print("Name is present in the dictionary")


# Dictionary comprehension
squares = {x: x*x for x in range(6)}
print("Squares dictionary:", squares)
