n=int(input("Enter a number : "))

sum=0
print("Sequence from 1 to",n)
for i in range(1,n+1):
    print(i)
    sum=sum+i
    
print("Even numbers between 1 to",n)
i=0
for i in range(1,n+1):
    if i%2==0:
        print(i)
i=0
print("Odd numbers between 1 to",n)
for i in range(1,n+1):
    if i%2!=0:
        print(i)

print("Sum of numbers from 1 to ",n,"=",sum)
#print(seq)
