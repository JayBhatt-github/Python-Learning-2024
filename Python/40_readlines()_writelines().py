# Open a file in read mode
file = open("example.txt", "r")

# Read the entire file at once
print("Reading the entire file at once:")
print(file.read())

# Close the file
file.close()

# Open the file in read mode
file = open("example.txt", "r")

# Read the file line by line
print("Reading the file line by line:")
for line in file.readlines():
    print(line)

# Close the file
file.close()

# Open a new file in write mode
# new_file = open("new_example.txt", "w")

# Write a list of lines to the file
# lines = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]
# new_file.writelines(lines)

# Close the file
# new_file.close()
