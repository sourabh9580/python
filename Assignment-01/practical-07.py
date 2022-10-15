# List of strings with 9 elements
A = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

# Slicing list into 3 equal parts
B = A[:len(A)//3]
C = A[len(A)//3:2*len(A)//3]
D = A[2*len(A)//3:]

print("----Main list----")
print("The list of strings is:", A)

print("----Sliced list----")
print("The first part of the list is:", B)
print("The second part of the list is:", C)
print("The third part of the list is:", D)

print("----Reversed list----")
print("Reverse the first part of the list:", B[::-1])
print("Reverse the second part of the list:", C[::-1])
print("Reverse the third part of the list:", D[::-1])