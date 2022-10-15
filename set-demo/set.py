# creating a set
print("Creating a set")
A = {1, 2, 3, 4, 5}
print(A)

# adding an element to a set
print("Adding an element to a set")
A.add(6)
print(A)

# adding multiple elements to a set
print("Adding multiple elements to a set")
A.update([7, 8, 9])
print(A)

# removing an element from a set
print("Removing an element from a set--remove()")
A.remove(6)
print(A)

# removing an element from a set
print("Removing an element from a set--discard()")
A.discard(2)
print(A)

# removing an element from a set
print("Removing an element from a set--pop()")
A.pop()
print(A)

# removing all elements from a set
print("Removing all elements from a set--clear()")
A.clear()
print(A)

# creating a set
print("Creating a set")
B = set([1, 2, 3, 4, 5])
print(B)

# checking if an element is in a set
print("Checking if an element is in a set")
print(2 in B)
print(7 in B)

# checking if an element is not in a set
print("Checking if an element is not in a set")
print(2 not in B)
print(7 not in B)

# checking if a set is a subset of another set
print("Checking if a set is a subset of another set")
print(A <= B)
print(A < B)
print(A >= B)
print(A > B)

# checking if two sets are equal
print("Checking if two sets are equal")
print(A == B)
print(A != B)

# creating an empty set
print("Creating an empty set")
C = set()
print(C)

# creating a set with a list
print("Creating a set with a list")
D = set([1, 2, 3, 4, 5])
print(D)

# creating a set with a tuple
print("Creating a set with a tuple")
E = set((1, 2, 3, 4, 5))
print(E)

# creating a set with a dictionary
print("Creating a set with a dictionary")
F = set({1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'})
print(F)

# creating a set with a set
print("Creating a set with a set")
G = set({1, 2, 3, 4, 5})
print(G)

# creating a set with a string
print("Creating a set with a string")
H = set('abcdefghijklmnopqrstuvwxyz')
print(H)

# creating a set with a range
print("Creating a set with a range")
I = set(range(1, 10))
print(I)

# creating a set with a range
print("Creating a set with a range")
J = set(range(1, 10, 2))
print(J)

# creating a set with a range
print("Creating a set with a range")
K = set(range(10, 1, -1))
print(K)
