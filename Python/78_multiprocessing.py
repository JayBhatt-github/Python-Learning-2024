# Multiprocessing in Python

import multiprocessing

# Define a function to print a message
def print_message():
    print("Hello, this is a multiprocessing example.")

if __name__ == '__main__':
    # Create a process
    process = multiprocessing.Process(target=print_message)

    # Start the process
    process.start()

    # Wait for the process to finish
    process.join()

    # Print a message after the process has finished
    print("Process has finished.")


# Other Example
from multiprocessing import Pool
def process_task(task):
    # Do some work here
    print("Task processed:", task)
if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with Pool(processes=4) as pool:
        results = pool.map(process_task, tasks)
    print("All tasks have been processed.")


# Explanation:

# In the above code, we have used the multiprocessing module to create a new process.
# We have defined a function print_message that prints a message.
# We have created a new process with the target function set to print_message.
# We have started the process and waited for it to finish using the join() method.
# After the process has finished, we print a message to indicate that the process has finished.

# The other example demonstrates the use of a Pool to process multiple tasks in parallel.
# We define a function process_task to process each task, and then use the Pool's map method to apply this function to each task.
# After all tasks have been processed, we print a message to indicate that all tasks have been processed.