# creating a dictionary
print("Creating a dictionary")
A = {'a': 1, 'b': 2, 'c': 3}
print(A)

# printing a value
print("Printing a value")
print(A['a'])

# adding a new key-value pair
print("Adding a new key-value pair")
A['d'] = 4
print(A)

# deleting a key-value pair
print("Deleting a key-value pair")
del A['b']
print(A)

# checking if a key exists
print("Checking if a key exists")
print('b' in A)

# dictionary methods
print("---Dictionary methods---")
# len()
print("len()")
print(len(A))

# copy()
print("copy()")
B = A.copy()
print(B)

# keys()
print("keys()")
print(A.keys())

# values()
print("values()")
print(A.values())

# items()
print("items()")
print(A.items())

# clear()
print("clear()")
A.clear()
print(A)

# pop()
print("pop()")
A = {'a': 1, 'b': 2, 'c': 3}
print(A.pop('a'))
print(A)

# popitem()
print("popitem()")
A = {'a': 1, 'b': 2, 'c': 3}
print(A.popitem())
print(A)

# update()
print("update()")
A = {'a': 1, 'b': 2, 'c': 3}
B = {'d': 4, 'e': 5, 'f': 6}
A.update(B)
print(A)

# setdefault()
print("setdefault()")
A = {'a': 1, 'b': 2, 'c': 3}
print(A.setdefault('a', 4))
print(A)
print(A.setdefault('d', 4))
print(A)

# get()
print("get()")
A = {'a': 1, 'b': 2, 'c': 3}
print(A.get('a'))
print(A.get('d'))
print(A.get('d', 4))

# dict()
print("dict()")
A = dict(a=1, b=2, c=3)
print(A)

# dict() with list of pairs
print("dict() with list of pairs")
A = dict([('a', 1), ('b', 2), ('c', 3)])
print(A)
