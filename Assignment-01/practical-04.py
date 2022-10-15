A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check(A):
    if A[0] == A[-1]:
        return True
    else:
        return False

print("The list of numbers is:", A)
print("The first number is:", A[0])
print("The last number is:", A[-1])
print("First and last number is same:", check(A))