#Printing a reverse * pyramid

n=int(input("Enter the number of steps you need for a pyramid :"))

for i in range(1,n+1):

    for k in range(1,2*i):
        print(" ",end="")

    for j in range(n-i):
        print("*",end="")

    # for k in range(1,2*i):
    #     print(" ",end="")

    print()