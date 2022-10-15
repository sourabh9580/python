# Display all prime numbers within a range
n = int(input("Enter a the range: "))
print("Prime numbers within 2 and {} are:".format(n))
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)