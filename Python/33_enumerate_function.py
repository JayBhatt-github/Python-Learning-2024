# enumurate function in python

ids = [1,2,3,4,5,6,7,8,9,10]

# Using enumerate to iterate through the list and print each id
for index, id in enumerate(ids):
    print(id)
    # Checking if the current index is at the halfway point of the list
    if(index == len(ids)/2-1):
      print("half list is printed") 

print("out of the loop")




# we solved this problem above using enumurate function

# ids = [1,2,3,4,5,6,7,8,9,10]
# index = 0

# for id in ids:
#     print(id)
#     if(index == len(ids)/2-1):
#       print("half list is printed") 
#       index +=1

# print("out of the loop")