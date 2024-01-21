# f-strings in Python

# f-strings provide a way to embed expressions inside string literals, using a minimal syntax
name = "John"
age = 30


# Using f-string to combine variables with text
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)


# It's also possible to perform operations inside an f-string
calculation = f"The result of 7 times 8 is {7 * 8}."
print(calculation)


# f-strings can also call functions
def get_greeting(name):
    return f"Hi {name}, welcome!"

print(get_greeting(name))


# Using f-strings with dictionaries
person = {'name': 'Alice', 'age': 25}
intro = f"The person's name is {person['name']} and their age is {person['age']}."
print(intro)

