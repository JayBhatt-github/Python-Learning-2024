# This is a simple example of a generator function in Python.
# The function 'my_generator' generates a sequence of numbers from 0 to 4.
# The 'yield' keyword is used to return a value from the generator.
# When the generator is called, it returns an iterator object.
# The 'next' function is used to get the next value from the iterator.

def my_generator():
    for i in range(5):
        yield i

# Create an instance of the generator.
gen = my_generator()

# Get the next value from the generator.
print(next(gen))

# Get the next value from the generator.
print(next(gen))

# Get the next value from the generator.
print(next(gen))

# Get the next value from the generator.
print(next(gen))

# Get the next value from the generator.
print(next(gen))
