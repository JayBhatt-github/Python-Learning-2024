# Multithreading in Python

import threading

# Define a function to print a message
def print_message():
    print("Hello, this is a multithreading example.")

# Create a thread
thread = threading.Thread(target=print_message)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

# Print a message after the thread has finished
print("Thread has finished.")

# # Other Example
# # Thread Pool Executor
# from concurrent.futures import ThreadPoolExecutor

# # Define a function to print a message
# def print_message():
#     print("Hello, this is a ThreadPoolExecutor example.")

# # Create a ThreadPoolExecutor
# with ThreadPoolExecutor() as executor:
#     # Submit the function to the executor
#     future = executor.submit(print_message)

# # Wait for the function to finish
# future.result()

# # Print a message after the function has finished
# print("Function has finished.")
