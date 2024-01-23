# for loop with else in python
# note: (The else block just after for/while is executed only when the loop is NOT terminated by a break statement.)

# Creating a list
numbers = [1, 2, 3, 4, 5]

# Iterating over the list
for number in numbers:
    print(number)
    # Breaking the loop if number is 3
    if number == 3:
        break
else:
    # This statement will not be executed as the loop is terminated by a break statement
    print("Loop ended")



# Another for loop with else
for number in numbers:
    print(number)
else:
    # This statement will be executed as the loop is not terminated by a break statement
    print("Loop ended")
