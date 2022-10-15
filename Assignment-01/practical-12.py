A = [1,5,6,10,20,40,200,50,100]
print("The list is:", A)

# display numbers which are divisible by 5 and stop the loop when the number is greater than 150
print("Numbers divisible by 5:")
for i in A:
    if i > 150:
        print("Value greater than 150 found! stopping the loop")
        break
    if i % 5 == 0:
        print(i)
