# creating the list
letters = ['a', 'b', 'c', 'd']

# printing the list
print(letters)

# printing length of the list
print(len(letters))

# printing a list element
print(letters[2])

# printing range of elements
print(letters[1:3])

# replacing an element
letters[2] = 'z'
print(letters)

# replacing range of elements
letters[1:3] = ['x', 'y']
print(letters)

# removing an element
letters.remove('x')
print(letters)

# removing range of elements
letters[1:3] = []
print(letters)

# adding an element at the end
letters.append('x')
print(letters)

# combining two lists
letters2 = ['A', 'B', 'C', 'D']
print(letters + letters2)

# creating nested list
numbers = [1, 2, 3, 4, 5]
alphanumeric = [letters, numbers]
print(alphanumeric)

# printing a list from a nested list
print(alphanumeric[0])

# printing an element from a nested list
print(alphanumeric[0][1])
