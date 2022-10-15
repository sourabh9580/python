# List of numbers with some repeated elements
A = [1, 2, 3, 4, 5, 8, 9, 10, 1, 2]

# Count the occurences of each element in the list and create a dictionary with the element as key and the count as value
B = {}
for i in A:
    if i in B:
        B[i] += 1
    else:
        B[i] = 1

print("----List of numbers with some repeated elements----")
print("The list of numbers is:", A)
print("----Occurences of each element in the list----")
print("The dictionary of occurences is:", B)
