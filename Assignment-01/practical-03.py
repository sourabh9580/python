# display characters at a even-numbered position in a string
A = input("Enter a string: ")

for i in range(len(A)):
    if i % 2 == 0:
        print(A[i], end=" ")