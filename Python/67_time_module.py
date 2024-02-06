import time

# Get the current time in seconds since the epoch
current_time = time.time()
print("Current time in seconds since the epoch:", current_time)

# Convert the current time to a readable format
readable_time = time.ctime(current_time)
print("Current time in readable format:", readable_time)

# Get the current local time
local_time = time.localtime(current_time)
print("Current local time:", local_time)

# Get the current UTC time
utc_time = time.gmtime(current_time)
print("Current UTC time:", utc_time)

# Get the current time in a specific format
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Current time in a specific format:", formatted_time)

# Sleep for 2 seconds
time.sleep(2)
print("Slept for 2 seconds")

# Get the current time after sleeping
current_time_after_sleep = time.time()
print("Current time after sleeping:", current_time_after_sleep)

# Calculate the time taken for sleeping
time_taken = current_time_after_sleep - current_time
print("Time taken for sleeping:", time_taken)
