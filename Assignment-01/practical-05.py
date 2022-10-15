A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("First list: ", A)
print("Second list: ", B)
C = []
for i in range(len(A)):
    if i % 2 == 0:
        C.append(B[i])
    else:
        C.append(A[i])

print("--After picking odd-index elements from first list and even-index elements from second list--")
print("The list of numbers is:", C)