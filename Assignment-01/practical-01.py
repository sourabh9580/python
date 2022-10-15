A = int(input("Enter first integer: "))
B = int(input("Enter second integer: "))

def product(A, B):
    C = A * B
    if C > 1000:
        print("The product is greater than 1000")
        D = A + B
        return C, D
    else:
        print("The product is less than or equal to 1000")
        return C

Result = product(A, B)

if(isinstance(Result, tuple)):
    print("The product is", Result[0])
    print("The sum of", A, "and", B, "is", Result[1])
else:
    print("The product is", Result)