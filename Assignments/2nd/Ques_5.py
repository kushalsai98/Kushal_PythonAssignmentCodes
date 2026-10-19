def mul_table(n,m):

    for i in range(1,m+1):
        print(n," * ",i," = ",n*i)

a=int(input("Enter which table you want to print : "))
b=int(input("Enter a number till which end you want to print the table : "))

mul_table(a,b)
    