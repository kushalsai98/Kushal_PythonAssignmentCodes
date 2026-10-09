# print("My name is kushal sai")

# #Printing a * pyramid pattern

# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

n=int(input("Enter a number: "))
f=1

for i in range(1,n+1):
    # if i == 0:
    #     continue
    f=f*i

fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1

print("The factorial of",n,"is",f,fact)

