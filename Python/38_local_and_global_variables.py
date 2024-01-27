
# Global variable
global_var = "i am global"

# Function to demonstrate local and global variables
def variable_demo():
    # Local variable
    local_var = "I am local "
    print("Inside the function, global_var is:", global_var)
    print("Inside the function, local_var is:", local_var)

# Call the function
variable_demo()

# Attempt to change the global variable from the function
def change_global():
    global global_var
    global_var = "I am the new global"

# Call the function to change the global variable
change_global()

# Print the global variable after attempting to change it from the function
print("changed the global, and Outside the function, global_var is:", global_var)

# Note: It is not a good practice to access and change the global variable value from the function
# It is better to pass the variable as an argument to the function if its value needs to be changed
