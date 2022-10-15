# creating a tuple
A = (1, 2, 3, 4, 5)

# printing the tuple
print(A)

# prtnting an element of the tuple
print(A[0])

# printing range of elements of the tuple
print(A[1:4])

# adding an element to the tuple
A = A + (6,)
print(A)

# adding multiple elements to the tuple
A = A + (7, 8, 9)
print(A)

# adding an element to the tuple at a specific position
A = A[:4] + (10,) + A[4:]
print(A)

# subtracting an element from the tuple
A = A[:4] + A[5:]
print(A)

# creating a tuple with a list
A = tuple(range(1, 10))
print(A)

# creating a tuple with a list
A = tuple(range(1, 10, 2))
print(A)

# deleting a tuple
del A
print(A)
