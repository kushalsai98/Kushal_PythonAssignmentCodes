def factorial():
    a=int(input("Enter a number to find out factorial : "))

    f=1
    for i in range(1,a+1):
        f=f*i

    # return f
    
    print("Factorial =",f)

# n=int(input("Enter a number to find out factorial : "))

# print("factorial =",factorial(n))