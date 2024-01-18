# taking input from the users
# Note : input() takes value as a string

a = input("Enter your name: ")
print("Hello ", a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x  + y)           # This will return x + y as a string because input() takes value as a string

print(int(x) + int(y))  # type casted both variable to return addition of var x and y