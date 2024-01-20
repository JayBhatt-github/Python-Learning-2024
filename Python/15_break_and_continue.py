# Python Break and Continue statements 

# Break in python
for i in range(10):
    if i == 5:
        break  # it will stop the loop when i is equal to 5
    print(i)

print("End of break statement demonstration\n")


# continue in python
for i in range(10):
    if i == 5:
        continue  # it will skip the rest of the loop when i is equal to 5 (it will not print number "5" it will start loop by taking i = 6")
    print(i)

print("End of continue statement demonstration")
