#Printing a * pyramid pattern 

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

#Printing a * pyramid pattern in reverse way
n=5
for i in range(n+1):
    j=i
    while (n-j)>0:
        print("*",end=" ")
        j=j+1
    print()

#Printing a number pyramid pattern

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
