# creating a frozen set
print("Creating a frozen set")
E = frozenset([1, 2, 3, 4, 5])
print(E)

# # adding an element to a frozen set
# print("Adding an element to a frozen set")
# E.add(6)
# print(E)

# # adding multiple elements to a frozen set
# print("Adding multiple elements to a frozen set")
# E.update([7, 8, 9])
# print(E)

# # removing an element from a frozen set
# print("Removing an element from a frozen set--remove()")
# E.remove(6)
# print(E)

# checking if an element is in a frozen set
print("Checking if an element is in a frozen set")
print(2 in E)
print(7 in E)

# checking if an element is not in a frozen set
print("Checking if an element is not in a frozen set")
print(2 not in E)
print(7 not in E)

# checking if a frozen set is a subset of another frozen set
print("Checking if a frozen set is a subset of another frozen set")
F = frozenset([1, 2, 3, 4, 5])
print(E <= F)
print(E < F)
print(E >= F)
print(E > F)

# checking if two frozen sets are equal
print("Checking if two frozen sets are equal")
print(E == F)

# copying a frozen set
print("Copying a frozen set")
G = E.copy()
print(G)

# creating a frozen set from a tuple
print("Creating a frozen set from a tuple")
I = frozenset((1, 2, 3, 4, 5))
print(I)

# creating a frozen set from a set
print("Creating a frozen set from a set")
J = frozenset(set([1, 2, 3, 4, 5]))
print(J)

# creating a frozen set from a dictionary
print("Creating a frozen set from a dictionary")
K = frozenset({1: "one", 2: "two", 3: "three", 4: "four", 5: "five"})
print(K)

# creating a frozen set from a string
print("Creating a frozen set from a string")
L = frozenset("hello")
print(L)

# creating a frozen set from a range
print("Creating a frozen set from a range")
M = frozenset(range(1, 10))
print(M)

# creating a frozen set from a range
print("Creating a frozen set from a range")
N = frozenset(range(1, 10, 2))
print(N)

# creating a frozen set from a range
print("Creating a frozen set from a range")
O = frozenset(range(10, 1, -1))
print(O)
