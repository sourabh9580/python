# receiving list of numbers from the user
A = int(input("Enter the number of elements in the list: "))
B = []
for i in range(A):
    B.append(int(input("Enter element: ")))

# Remove the element at index 4 and add it to 2nd position and at the end of the list
print("The list of numbers is:", B)
if len(B) <= 4:
    print("Please enter at least 5 elements")
else:
    C = B.pop(4)
    B.insert(1, C)
    B.append(C)
    print("New list of numbers is:", B)
