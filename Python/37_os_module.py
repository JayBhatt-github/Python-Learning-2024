import os

# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)


# Create a new directory
# new_directory = "new_directory"
# os.mkdir(new_directory)
# print("Directory created successfully")


# Check if a file exists
file_name = "example.txt"
if os.path.exists(file_name):
    print(f"The file {file_name} exists")
else:
    print(f"The file {file_name} does not exist")


# List all files and directories in the current directory
print("Files and directories in the current directory:")
print(os.listdir())


# Remove the new directory
# os.rmdir(new_directory)
# print("Directory removed successfully")


# Generate code for renaming and making bulk folders with names

# Rename a directory
# old_directory_name = "old_directory"
# new_directory_name = "new_directory"
# os.rename(old_directory_name, new_directory_name)
# print("Directory renamed successfully")

# Make bulk folders with names
# folder_names = ["folder1", "folder2", "folder3"]
# for folder_name in folder_names:
#     os.mkdir(folder_name)
#     print(f"Folder {folder_name} created successfully")

