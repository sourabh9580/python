n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum += i

print("The sum of all numbers between 1 and {} is {}".format(n,sum))